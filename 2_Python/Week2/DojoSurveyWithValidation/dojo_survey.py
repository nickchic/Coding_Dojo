from flask import Flask, render_template, request, redirect, session, flash
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
    form_complete = True
    if len(request.form['name']) < 1:
        flash("Name cannot be blank")
        form_complete = False
    if len(request.form['comment']) > 120:
        flash("Comment must be less than 120 characters")
        form_complete = False
    elif len(request.form['comment']) < 1:
        flash("Comment cannot be blank")
        form_complete = False
    if form_complete:
        return redirect('/results')
    else:
        return redirect('/')


app.run(debug=True)
