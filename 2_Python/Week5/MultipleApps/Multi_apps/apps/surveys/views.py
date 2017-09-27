from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all surveys"
    return HttpResponse(response)

def new(request):
    response = "Placeholder for users to add a new survey"
    return HttpResponse(response)
