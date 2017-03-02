from flask import Flask, render_template, redirect, request, flash, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    if len(request.form['name']) < 1:
        flash(u"Name cannot be empty!", 'name')
    if len(request.form['comment']) < 1:
        print "working"
        flash(u"Hey, you need to write in a comment here!", 'comm')
    if len(request.form['comment']) > 120:
        flash(u"Your comment is too long.", 'comm')
    return render_template('result.html')

app.run(debug=True)
