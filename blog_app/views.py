from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class ListBlogView(ListView):
    model = Post
    template_name = 'blog.html'
