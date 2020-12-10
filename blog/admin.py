from django.contrib import admin
from django.db import models
from .models import Post
from tinymce.widgets import TinyMCE

class PostAdmin(admin.ModelAdmin):
    model=Post

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
        }

admin.site.register(Post, PostAdmin)
