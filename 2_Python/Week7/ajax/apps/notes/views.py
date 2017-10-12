from django.shortcuts import render, HttpResponse, redirect
from .models import Note

def index(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/index.html')

def add(request):
    new_note = Note(text=request.POST['text'])
    new_note.save()
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/all_notes.html', context)
