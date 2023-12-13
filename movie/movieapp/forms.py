from django import forms
from .models import movie_list


class MovieForm(forms.ModelForm):
    class Meta:
        model = movie_list
        fields = ['name', 'img', 'desc', 'year']

