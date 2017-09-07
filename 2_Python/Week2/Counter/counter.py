from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session["num"] += 1
    return render_template('index.html', num=session['num'])

@app.route('/two')
def incriment_two():
    session["num"] += 2
    return redirect('/')

@app.route('/reset')
def reset():
    session["num"] = 0
    return redirect('/')

app.run(debug=True)
