from flask import Flask, render_template, request, redirect
app = Flask(__name__)

name = 'default'
dojo = 'default'
language = 'default'
comment = 'default'

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/results')
def display_results():
    print "Results page loaded", name, language, dojo, comment
    return render_template('results.html', name=name, dojo=dojo, language=language, comment=comment)

@app.route('/action', methods=['POST'])
def submit_form():
    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comment = request.form['comment']
    print "Form Submitted", name, language, dojo, comment
    return redirect('/results')

app.run(debug=True)
