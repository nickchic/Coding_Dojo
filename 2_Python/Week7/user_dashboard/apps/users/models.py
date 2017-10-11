from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def user_validation(self, postdata):
        errors = {}
        if len(postdata['first_name']) < 2:
            errors['first_name'] = "First name must be at lease 2 characters long"
        if len(postdata['last_name']) < 2:
            errors['last_name'] = "Last name must be at lease 2 characters long"
        if len(postdata['email']) < 1 or not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Email must be valid"
        if len(postdata['password']) < 8:
            errors['password'] = "Password must be 8 characters long"
        if not postdata['password'] == postdata['confirm']:
            errors['confirm'] = "Password and confirm password must match"
        return errors
    def info_validation(self, postdata):
        errors = {}
        if len(postdata['first_name']) < 2:
            errors['first_name'] = "First name must be at lease 2 characters long"
        if len(postdata['last_name']) < 2:
            errors['last_name'] = "Last name must be at lease 2 characters long"
        if len(postdata['email']) < 1 or not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Email must be valid"
        return errors
    def password_validation(self, postdata):
        errors = {}
        if len(postdata['password']) < 8:
            errors['password'] = "Password must be 8 characters long"
        if not postdata['password'] == postdata['confirm']:
            errors['confirm'] = "Password and confirm password must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    desc = models.TextField()
    admin = models.BooleanField()
    password_hash = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, related_name="written_messages")
    recipient = models.ForeignKey(User, related_name="wall_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, related_name="comments")
    message = models.ForeignKey(Message, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
