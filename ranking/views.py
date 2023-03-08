from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Swordfighter, Comment, User
from .forms import SwordfighterForm, CommentForm
from django.db.models import Q

class Helper():
    def user_permitted(self, request, swordfighter):
        if not request.user.username == swordfighter.suggested_by:
            if not swordfighter.status == 1:
                if not swordfighter.status == 2:
                    return False
        return True
    
    def queryset_not_empty(self, queryset):
        if queryset.count() > 0:
            return True
        else:
            return False

    def check_if_draft(self, swordfighter):
        if swordfighter.status == 1 or swordfighter.status == 2:
            return False
        else:
            return True



class LandingPage(View):
    def get(self, request):
        return render(
            request,
            "landing.html"
        )


class SwordfighterList(View):
    def get(self, request):
        swordfighters = Swordfighter.objects.filter(Q(status=1) | Q(status=2)).annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
        current_user = self.request.user.id
        upvoted_fighters = []
        for swordfighter in swordfighters:
            if swordfighter.upvotes.filter(id=current_user).exists():
                upvoted_fighters.append(swordfighter.name)

        return render(
            request,
            "ranking.html",
            {
                'swordfighters': swordfighters,
                'upvoted_fighters': upvoted_fighters,
            }
        )


class SwordfighterDetail(View, Helper):
    queryset = Swordfighter.objects

    def get(self, request, slug, *args, **kwargs):
        swordfighter = get_object_or_404(self.queryset, slug=slug)
        if not self.user_permitted(request, swordfighter):
            return render(
                request,
                '403.html'
            )
        is_draft = self.check_if_draft(swordfighter)

        swordfighter_comments = Comment.objects.filter(swordfighter=swordfighter) 
        current_user = request.user
        flagged_comments = []
        for comment in swordfighter_comments:
            if comment.flags.filter(id=self.request.user.id):
                flagged_comments.append(comment.id)
        if request.user.is_authenticated:
            button_name='Submit'
        else:
            button_name='Login to comment'

        comments = Comment.objects.filter(swordfighter=swordfighter)
        return render(
            request,
            "character_page.html",
            {
                "swordfighter": swordfighter,
                "comments": comments,
                "comment_form": CommentForm(),
                "flagged_comments": flagged_comments,
                "current_user": current_user,
                "button_name": button_name,
                "is_draft": is_draft,
            }
        )
    
    def post(self, request, slug, *args, **kwargs):
        
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))

        swordfighter = get_object_or_404(self.queryset, slug=slug)
        if self.check_if_draft(swordfighter):
            return render(
                request,
                '403.html'
            )
        else:
            is_draft = False

        comment_form = CommentForm(request.POST)
        swordfighter_comments = Comment.objects.filter(swordfighter=swordfighter) 
        current_user = request.user

        flagged_comments = []
        for comment in swordfighter_comments:
            if comment.flags.filter(id=self.request.user.id):
                flagged_comments.append(comment.id)
        if request.user.is_authenticated:
            button_name='Submit'
        else:
            button_name='Login to comment'

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
                "button_name": button_name,
                "flagged_comments": flagged_comments,
                "current_user": current_user,
                "button_name": button_name,
                "is_draft": is_draft,
            }
        )
 
 

class SwordfighterUpvote(View, Helper):
    def post(self, request, slug):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        swordfighter = get_object_or_404(Swordfighter, slug=slug)
        if self.check_if_draft(swordfighter):
            return render(
                request,
                '403.html'
            )


        if swordfighter.upvotes.filter(id=request.user.id).exists():
            swordfighter.upvotes.remove(request.user)
        else:
            swordfighter.upvotes.add(request.user)
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class Contribute(View, Helper):

    def get(self, request):
        if not request.user.is_authenticated:
            button_name = 'Log in'
        else:
            button_name = 'Submit'
        
        suggestions = Swordfighter.objects.filter(suggested_by=request.user.username)
        render_suggestions = self.queryset_not_empty(suggestions)


        return render(
            request,
            "contribute.html",
            {
                "swordfighter_form": SwordfighterForm(),
                "suggestions": suggestions,
                "button_name": button_name,
                "render_suggestions": render_suggestions,
            }
        )
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))

        suggestions = Swordfighter.objects.filter(suggested_by=request.user.username)
        render_suggestions = self.queryset_not_empty(suggestions)
        swordfighter_form = SwordfighterForm(request.POST, request.FILES)
        button_name = 'Submit'

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
                "suggestions": suggestions,
                "button_name": button_name,
                "render_suggestions": render_suggestions,
            }
        )
    

class Delete_swordfighter(View, Helper):

    def get(self, request, slug, *args, **kwargs):
        queryset = Swordfighter.objects
        swordfighter = get_object_or_404(queryset, slug=slug)
        if not self.user_permitted(request, swordfighter):
            return render(
                request,
                '403.html'
            )

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
    



class edit_swordfighter(View, Helper):
    
    def get(self, request, slug):

        swordfighter = Swordfighter.objects.get(slug=slug)
        if not self.user_permitted(request, swordfighter):
            return render(request,'403.html')

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


