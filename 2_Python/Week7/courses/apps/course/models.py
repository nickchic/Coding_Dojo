from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def course_validation(self, postdata):
        errors = {}
        if len(postdata['name']) < 5:
            errors['name'] = "Name must be 5 characters long"
        if len(postdata['desc']) < 15:
            errors['desc'] = "Description must be 15 characters long"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
