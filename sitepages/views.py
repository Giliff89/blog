# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def contact(request):
    return render(request, 'sitepages/contact.html')


def about(request):
    return render(request, 'sitepages/about.html')
