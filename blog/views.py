from django.shortcuts import render
from django.views import generic

from .models import Post


class BlogIndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

