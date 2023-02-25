from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import swordfighter

class swordfighterList(generic.ListView):
    model = swordfighter
    template_name = 'index.html'


class swordfighterDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = swordfighter.objects
        character = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "character_page.html",
            {
                "character": character
            }
        )

