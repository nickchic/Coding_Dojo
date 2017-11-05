# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User, UserManager
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    content = models.TextField()
    reviewer = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
