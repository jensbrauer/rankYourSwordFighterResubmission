from .models import Swordfighter
from django import forms

class SwordfighterForm(forms.ModelForm):
    class Meta:
        model = Swordfighter
        fields = ('name', 'appears_on', 'description', 'profile_img')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'appears_on' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'profile_img' : forms.FileInput(attrs={'class': 'form-control', 'id' : 'img_upload'})
        }
