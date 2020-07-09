# Create your models here.
from django.contrib import auth
from django.db import models
from django.utils import timezone
from groups.models import GroupMember


class User(auth.models.User, auth.models.PermissionsMixin):
    # membership= models.ManyToManyField(Group,through="GroupMember")
    def __str__(self):
        return "@{}".format(self.username)
