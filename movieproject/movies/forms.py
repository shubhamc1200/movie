from django import forms
from . import models

class CreateMoviePage(forms.ModelForm):
    class Meta:
        model=models.Movie
        fields=['title','movie_url','body','thumb','genre']

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea,label='') #in order to avoid label 'text:'
    class Meta:
        model = models.Comment
        fields = ['text']
