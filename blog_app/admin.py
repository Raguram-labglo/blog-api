from django.contrib import admin
from .models import *

class Postview(admin.ModelAdmin):
    list_display = ['user', 'title', 'body', 'created']
admin.site.register(Post, Postview)
admin.site.register(Comment)
admin.site.register(Feed)
