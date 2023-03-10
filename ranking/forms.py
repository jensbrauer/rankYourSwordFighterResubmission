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
    
    def __is_only_letters(self, name):
        allowed_letters = 'abcdefghijklmnopqrstuvwxyz '
        for letter in str(name):
            if letter.lower() not in allowed_letters:
                return False
        return True

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not self.__is_only_letters(name):
            raise forms.ValidationError("The name of a fighter can only include English letters.")
        return name

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content' : forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
