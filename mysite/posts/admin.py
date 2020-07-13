from django.contrib import admin

from . import models

myModels = [models.Post,models.Comment]  # iterable list
admin.site.register(myModels)

