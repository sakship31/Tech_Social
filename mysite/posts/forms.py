from django import forms

from posts import models


class PostForm(forms.ModelForm):
    class Meta:
        # fields = ("message", "group")
        fields = ('question','description','picture')
        model = models.Post




class CommentForm(forms.ModelForm):
    class Meta:
        # fields = ("message", "group")
        fields = ('comment','pic')
        model = models.Comment
