from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random
import time
from time import gmtime, strftime

@app.route('/')
def index():
    try:
        session['gold']
    except:
        session['gold'] = 0
    try:
        session['log']
    except:
        session['log'] = []

    print "Gold = {}".format(session['gold'])
    print "log length = {}".format(len(session['log']))
    return render_template('index.html', gold=session['gold'], log=session['log'])

@app.route('/process_money', methods=['POST'])
def submit():
    if request.form['building'] == "farm":
        print "farm";
        amountAwarded = random.randrange(9,21)
        session['gold'] += amountAwarded
        session['log'].append("You got {} from the farm! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    elif request.form['building'] == "cave":
        print "cave";
        amountAwarded = random.randrange(4,11)
        session['gold'] += amountAwarded
        session['log'].append("You got {} from the cave! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    elif request.form['building'] == "house":
        print "house";
        amountAwarded = random.randrange(1,6)
        session['gold'] += amountAwarded
        session['log'].append("You got {} from the house! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    elif request.form['building'] == "casino":
        print "casino";
        if session['gold'] == 0:
            print "no money"
            session['gold'] = 0
            session['log'].append("You have nothing to bet! ({})".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
        else:
            print "calculating amountAwarded"
            amountAwarded = random.randrange(0,51)
            if bool(random.getrandbits(1)):
                print "win at casino"
                session['gold'] += amountAwarded
                session['log'].append("You won {} at the casino! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
            else:
                print "lose at casino"
                session['gold'] -= amountAwarded
                if session['gold'] < 0:
                    session['gold'] = 0
                    session['log'].append("You lost EVERYTHING at the casino! ({})".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                else:
                    session['log'].append("You lost {} at the casino! ({})".format(amountAwarded, strftime("%Y-%m-%d %H:%M:%S", gmtime())))


    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['log'] = []
    return redirect('/')


app.run(debug=True)
