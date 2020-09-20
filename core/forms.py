from django import forms

from core.models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
