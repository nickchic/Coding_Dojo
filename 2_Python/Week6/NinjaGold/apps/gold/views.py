from django.shortcuts import render, redirect

import random
import time
from time import gmtime, strftime

def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    try:
        request.session['log']
    except:
        request.session['log'] = []

    print "Gold = {}".format(request.session['gold'])
    print "log length = {}".format(len(request.session['log']))
    return render(request, 'gold/index.html')

def process_money(request):
    if request.POST['building'] == "farm":
        print "farm";
        amountAwarded = random.randrange(9,21)
        request.session['gold'] += amountAwarded
        request.session['log'].append("You got {} from the farm! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    elif request.POST['building'] == "cave":
        print "cave";
        amountAwarded = random.randrange(4,11)
        request.session['gold'] += amountAwarded
        request.session['log'].append("You got {} from the cave! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    elif request.POST['building'] == "house":
        print "house";
        amountAwarded = random.randrange(1,6)
        request.session['gold'] += amountAwarded
        request.session['log'].append("You got {} from the house! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    elif request.POST['building'] == "casino":
        print "casino";
        if request.session['gold'] == 0:
            print "no money"
            request.session['gold'] = 0
            request.session['log'].append("You have nothing to bet! ({})".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
        else:
            print "calculating amountAwarded"
            amountAwarded = random.randrange(0,51)
            if bool(random.getrandbits(1)):
                print "win at casino"
                request.session['gold'] += amountAwarded
                request.session['log'].append("You won {} at the casino! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
            else:
                print "lose at casino"
                request.session['gold'] -= amountAwarded
                if request.session['gold'] < 0:
                    request.session['gold'] = 0
                    request.session['log'].append("You lost EVERYTHING at the casino! ({})".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                else:
                    request.session['log'].append("You lost {} at the casino! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    return redirect('/gold')

def reset(request):
    print "reset"
    request.session['gold'] = 0
    request.session['log'] = []
    return redirect('/gold')

# Create your views here.
