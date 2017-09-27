from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    print "Create"
    return redirect(index)

def number(request, number):
    response = 'Placeholder to DISPLAY blog {}'.format(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'Placeholder to EDIT blog {}'.format(number)
    return HttpResponse(response)

def delete(request, number):
    print "Delete {}".format(number)
    return redirect(index)
