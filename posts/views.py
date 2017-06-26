# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models


def home(request):

    posts = models.Post.objects.order_by('publish_date')

    return render(request, 'posts/home.html', {'posts': posts})
