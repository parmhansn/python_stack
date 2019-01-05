from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'send_help'

@app.route('/')
def visits():
	if 'visits' in session:
		session['visits'] = session.get('visits') +1
	else:
		session['visits'] = 1
	return "Total visits: {}".format(session.get('visits'))

@app.route('/delete_visits')
def delete_visits():
	session.pop('visits', None) #deleted visits
	return 'Visits deleted'








app.run(debug=True) 
