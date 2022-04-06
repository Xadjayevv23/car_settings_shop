from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPostModel


class BlogListView(ListView):
    model = BlogPostModel
    template_name = "main/blog_list.html"
    context_object_name = 'posts'
