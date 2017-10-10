from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, CourseManager

def index(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'course/index.html', context)

def remove_confirm(request, id_num):
    course_to_remove = Course.objects.get(id=id_num)
    context = {
        'course':course_to_remove
    }
    return render(request, 'course/remove_confirm.html', context)

def remove(request, id_num):
    course_to_remove = Course.objects.get(id=id_num)
    course_to_remove.delete()
    return redirect('/')

def add_course(request):
    errors = Course.objects.course_validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    else:
        new_course = Course(name=request.POST['name'], desc=request.POST['desc'])
        new_course.save()
        return redirect('/')
