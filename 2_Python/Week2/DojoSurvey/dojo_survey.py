from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/results')
def display_results():
    print "Results page loaded", session['name'], session['language'], session['dojo'], session['comment']
    return render_template('results.html', name=session['name'], dojo=session['dojo'], language=session['language'], comment=session['comment'])

@app.route('/action', methods=['POST'])
def submit_form():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print "Form Submitted", session['name'], session['language'], session['dojo'], session['comment']
    return redirect('/results')

app.run(debug=True)
