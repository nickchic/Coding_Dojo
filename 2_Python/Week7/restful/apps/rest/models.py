from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserValidations(models.Manager):
    def user_validate(self, postdata):
        errors = {}
        if len(postdata['email']) < 1 or not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Please enter a valid email"
        if len(postdata['first_name']) < 1:
            errors['first_name'] = "First Name must not be blank"
        if len(postdata['last_name']) < 1:
            errors['last_name'] = "Last Name must not be blank"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserValidations()
