from .models import Swordfighter
from django import forms

class SwordfighterForm(forms.ModelForm):
    class Meta:
        model = Swordfighter
        fields = ('name', 'appears_on', 'description', 'profile_img')
