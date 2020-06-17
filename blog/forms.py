from django.forms import ModelForm
from blog import models
from django import forms

class PostCreateForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'post_image']