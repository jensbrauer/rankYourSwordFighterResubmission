from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Swordfighter, Comment, User
from .forms import SwordfighterForm, CommentForm
from django.db.models import Q


class LandingPage(View):
    def get(self, request):
        return render(
            request,
            "landing.html"
        )

class SwordfighterList(generic.ListView):
    model = Swordfighter
    queryset = Swordfighter.objects.filter(Q(status=1) | Q(status=2)).annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
    template_name = 'ranking.html'


class SwordfighterDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Swordfighter.objects
        swordfighter = get_object_or_404(queryset, slug=slug)
        swordfighter_comments = Comment.objects.filter(swordfighter=swordfighter) 
        flagged_comments = []
        for comment in swordfighter_comments:
            if comment.flags.filter(id=self.request.user.id):
                flagged_comments.append(comment.id)

        comments = Comment.objects.filter(swordfighter=swordfighter)
        return render(
            request,
            "character_page.html",
            {
                "swordfighter": swordfighter,
                "comments": comments,
                "comment_form": CommentForm(),
                "flagged_comments": flagged_comments,
            }
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Swordfighter.objects
        swordfighter = get_object_or_404(queryset, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.submitted_by = request.user.username
            comment = comment_form.save(commit=False)
            comment.swordfighter = swordfighter
            comment = comment_form.save()
        else:
            comment_form = CommentForm()
        
        comments = Comment.objects.filter(swordfighter=swordfighter)

        return render(
            request,
            "character_page.html",
            {
                "swordfighter": swordfighter,
                "comments": comments,
                "comment_form": CommentForm(),
            }
        )

class SwordfighterUpvote(View):

    def post(self, request, slug):
        swordfighter = get_object_or_404(Swordfighter, slug=slug)

        if swordfighter.upvotes.filter(id=request.user.id).exists():
            swordfighter.upvotes.remove(request.user)
        else:
            swordfighter.upvotes.add(request.user)
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class Contribute(View):

    def get(self, request):
        suggestions = Swordfighter.objects.filter(suggested_by=request.user.username)
    
        return render(
            request,
            "contribute.html",
            {
                "swordfighter_form": SwordfighterForm(),
                "suggestions": suggestions
            }
        )
    
    def post(self, request):
        suggestions = Swordfighter.objects.filter(suggested_by=request.user.username)
        swordfighter_form = SwordfighterForm(request.POST, request.FILES)

        if swordfighter_form.is_valid():
            swordfighter_form.instance.suggested_by = request.user.username
            swordfighter_form.instance.slug = swordfighter_form.cleaned_data['name'].replace(" ", "_")
            swordfighter = swordfighter_form.save()
        else:
            swordfighter_form = SwordfighterForm()

        return render(
            request,
            "contribute.html",
            {
                "swordfighter_form": SwordfighterForm(),
                "suggestions": suggestions
            }
        )
    

class Delete_swordfighter(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Swordfighter.objects
        swordfighter = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "ru_sure_delete.html",
            {
                "swordfighter": swordfighter
            }
        )
    
    def post(self, request, slug):
        instance = Swordfighter.objects.get(slug=slug)
        instance.delete()
        return redirect('contribute')
    

class edit_swordfighter(View):
    
    def get(self, request, slug):
        swordfighter = Swordfighter.objects.get(slug=slug)
        edit_form = SwordfighterForm(instance=swordfighter)
        return render(
            request,
            "edit_swordfighter.html",
            {
                "edit_form": edit_form,
                "swordfighter": swordfighter
            }
        )
    
    def post(self, request, slug):
        swordfighter = Swordfighter.objects.get(slug=slug)
        submit_form = SwordfighterForm(request.POST, request.FILES, instance=swordfighter)
        submit_form.save()
        return redirect('contribute')

class FlagComment(View):
    
    def post(self, request, id, *args, **kwargs):
        comment = Comment.objects.get(id=id)
        if comment.flags.filter(id=request.user.id).exists():
            comment.flags.remove(request.user)
        else:
            comment.flags.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteComment(View):
    
    def post(self, request, id):
        instance = Comment.objects.get(id=id)
        instance.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))