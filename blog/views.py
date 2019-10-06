# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from my_markdown import markdown

def index(request):
    template = loader.get_template('blog/Home.html')
    posts = Post.objects.order_by('-id')[:10]

    post = posts[0]
    recents = []
    for p in posts:
        recents.append({
            "title": p.title,
            "id": p.id,
        })
    context = {
        "title": post.title,
        "date": post.date,
        "author": post.author,
        "content": (post.content,markdown.markdown_to_html(post.content))[post.useMarkdown],
        "recents": recents
    }
    return HttpResponse(template.render(context,request))

def post(request,postId):
    template = loader.get_template('blog/Home.html')
    posts = Post.objects.order_by('-id')[:10]
    post = Post.objects.get(pk=postId)
    recents = []
    for p in posts:
        recents.append({
            "title": p.title,
            "id": p.id,
        })
    context = {
        "title": post.title,
        "date": post.date,
        "author": post.author,
        "content": post.content,
        "recents": recents
    }
    return HttpResponse(template.render(context, request))