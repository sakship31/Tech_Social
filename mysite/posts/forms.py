from django import forms

from posts import models


class PostForm(forms.ModelForm):
    class Meta:
        # fields = ("message", "group")
        fields = ('question','description')
        model = models.Post




class CommentForm(forms.ModelForm):
    class Meta:
        # fields = ("message", "group")
        fields = ('comment',)
        model = models.Comment
