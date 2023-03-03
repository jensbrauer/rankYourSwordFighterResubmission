from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Swordfighter
from .forms import SwordfighterForm
from django.db.models import Q

class SwordfighterList(generic.ListView):
    model = Swordfighter
    queryset = Swordfighter.objects.filter(Q(status=1) | Q(status=2)).annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
    template_name = 'index.html'


class SwordfighterDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Swordfighter.objects
        swordfighter = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "character_page.html",
            {
                "swordfighter": swordfighter
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
        submit_form = SwordfighterForm(request.POST, instance=swordfighter)
        submit_form.save()
        return redirect('contribute')
