from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka

from groups.models import  Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    question = models.CharField(max_length=255)
    # question_html = models.TextField(editable=False)
    description=models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE,)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        self.question_html = misaka.html(self.question)
        self.description_html = misaka.html(self.description)  
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "question"]

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    text = models.TextField()
    text_html = models.TextField(editable=False)
    user = models.ForeignKey(User, related_name="comments",on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.text_html = misaka.html(self.text)  
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("posts:single" , kwargs={"slug": self.slug})
        return reverse("posts:single" , kwargs={"username":self.post.user.username,"pk":self.post.pk})

    def __str__(self):
        return self.text

