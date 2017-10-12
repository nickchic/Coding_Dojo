from django.shortcuts import render, HttpResponse, redirect
from .models import Note_Title

def index(request):
    context = {
        'notes': Note_Title.objects.all()
    }
    return render(request, 'notes_two/index.html', context)

def add(request):
    new_note = Note_Title(title=request.POST['title'])
    new_note.save()
    context = {
        'notes': Note_Title.objects.all()
    }
    return render(request, 'notes_two/all_notes.html', context)

def add_text(request):
    print 'add_text'
    note_to_edit = Note_Title.objects.get(id=request.POST['id'])
    note_to_edit.text = request.POST['text']
    note_to_edit.save()
    return HttpResponse('')

def delete(request):
    return render(request, 'notes_two/all_notes.html', context)
