from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","content")

    content = forms.CharField(widget=TinyMCE())