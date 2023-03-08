from .models import Swordfighter, Comment
from django import forms

class SwordfighterForm(forms.ModelForm):
    class Meta:
        model = Swordfighter
        fields = ('name', 'appears_on', 'description', 'profile_img')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'appears_on' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'profile_img' : forms.FileInput(attrs={'class': 'form-control', 'id' : 'img_upload'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content' : forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
