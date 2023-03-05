from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    #  list of posts status=1(approved) and ordered by when created
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # name of html file that our view will be rendered to
    template_name = "index.html"
    # paginate(separate into pages) limit 6 means will only show 6 posts
    # on front page, any more django will auto do page nav
    paginate_by = 6
