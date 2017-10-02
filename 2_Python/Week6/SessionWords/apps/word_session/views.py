from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import strftime

def index(request):
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []
        
    print request.session['words']

    return render(request, "word_session/index.html")

def add_word(request):

    form_complete = True
    #Checks that the name is filled out
    if len(request.POST['word']) < 1:
        print "no name"
        form_complete = False
    #Checks that a color was picked
    try:
        request.POST['color']
    except KeyError:
        print "no color"
        form_complete = False

    if not form_complete:
        print "form is no good"
        return redirect("/")

    #adds in data is form is complete

    class_string = str(request.POST['color'])
    try:
        if request.POST['big']:
            class_string += " big"
    except KeyError:
        pass

    time = datetime.now()
    time_string = time.strftime("%Y-%m-%d %H:%M:%S")
    description_string = "added {}".format(time_string)

    new_word = {
     'word':request.POST['word'],
     'description': description_string,
     'classes': class_string
    }

    print new_word

    request.session['words'].append(new_word)
    print request.session['words']
    request.session.modified = True
    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")
