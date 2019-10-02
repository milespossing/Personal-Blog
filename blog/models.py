# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
