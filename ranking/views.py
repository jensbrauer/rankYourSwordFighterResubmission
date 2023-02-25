from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Swordfighter

class SwordfighterList(generic.ListView):
    model = Swordfighter
    template_name = 'index.html'


class SwordfighterDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Swordfighter.objects
        character = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "character_page.html",
            {
                "character": character
            }
        )

class SwordfighterUpvote(View):

    def post(self, request, slug):
        swordfighter = get_object_or_404(Swordfighter, slug=slug)

        if swordfighter.upvotes.filter(id=request.user.id).exists():
            swordfighter.upvotes.remove(request.user)
        else:
            swordfighter.upvotes.add(request.user)
        
        return HttpResponseRedirect(reverse('home', args=[]))