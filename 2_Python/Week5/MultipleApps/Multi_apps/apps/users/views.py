from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all the list of users"
    return HttpResponse(response)

def new(request):
    print "New"
    return redirect(register)

def login(request):
    response = "Placeholder for users to login"
    return HttpResponse(response)

def register(request):
    response = "Placeholder for users to create a new user record"
    return HttpResponse(response)
