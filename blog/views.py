# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    template = loader.get_template('blog/Home.html')
    post = Post.objects.last()
    context = {
        "title": post.title,
        "date": post.date,
        "author": post.author,
        "content": post.content,
    }
    return HttpResponse(template.render(context,request))