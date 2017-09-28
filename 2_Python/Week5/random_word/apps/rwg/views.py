from django.shortcuts import render, HttpResponse, redirect
import random, string

# Create your views here.
def index(request):
    try:
        request.session['attempts'] += 1
    except KeyError:
        request.session['attempts'] = 1

    rand_word = ""
    for x in range(0,14):
        rand_word += random.choice(string.letters)

    print rand_word
    request.session['word'] = rand_word

    return render(request, "rwg/index.html")


def reset(request):
    request.session['attempts'] = 0
    return redirect("/random_word")
