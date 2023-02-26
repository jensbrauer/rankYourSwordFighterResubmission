from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Swordfighter
from .forms import SwordfighterForm

class SwordfighterList(generic.ListView):
    model = Swordfighter
    queryset = Swordfighter.objects.annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
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
        return render(
            request,
            "contribute.html",
            {
                "swordfighter_form": SwordfighterForm()
            }
        )