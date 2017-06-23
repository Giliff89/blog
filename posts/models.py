# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
