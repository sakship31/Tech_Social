#from django.contrib import admin

# Register your models here.
from django.contrib import admin

from . import models


# class GroupMemberInline(admin.TabularInline):
#     model = models.GroupMember



# admin.site.register(models.Group)
myModels = [models.Group,models.GroupMember]  # iterable list
admin.site.register(myModels)
