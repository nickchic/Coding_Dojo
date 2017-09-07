from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random

@app.route('/')
def index():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

    if session['counter'] == 1:
        # resets everything to play again
        session['number'] = random.randrange(0, 101)
        session['guess'] = False
        session['clueMessage'] = ""
    print session['counter']
    print session['number']
    print session['guess']
    print session['clueMessage']
    return render_template('index.html', guess=session['guess'], clue=session['clueMessage'])



@app.route('/action', methods=['POST'])
def submit_form():
    print "Guess = {} Number = {}".format(request.form['guess'], session['number'])
    if int(request.form['guess']) > session['number']:
        print "Too high"
        session['guess'] = False
        session['clueMessage'] = "Too High, Guess Again!"
    elif int(request.form['guess']) < session['number']:
        print "Too low"
        session['guess'] = False
        session['clueMessage'] = "Too Low, Guess Again!"
    elif int(request.form['guess']) == session['number']:
        print "correct"
        session['guess'] = True
        session['clueMessage'] = "Correct! it Took you {} tries, Play again?".format(session['counter'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def play_again():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
