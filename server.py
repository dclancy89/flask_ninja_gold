import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, Markup
app = Flask(__name__)
app.secret_key = 'kfjifo32wh0f32hiofsnokfu09rr324u0rh23o4ruyc80243n85b092v345782390c5n2380u45b238'

@app.route('/')
def index():
	if session.get('gold') == None:
		session['gold'] = 0


	if session.get('activities') == None:
		session['activities'] = []

	print session['activities']

	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	building = request.form['building']
	if building == 'farm':
		rand = random.randrange(10, 21)
		session['gold'] += rand
		session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
	elif building == 'cave':
		rand = random.randrange(5, 11)
		session['gold'] += rand
		session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
	elif building == 'house':
		rand = random.randrange(2, 6)
		session['gold'] += rand
		session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
		
	elif building == 'casino':
		if session['gold'] >= 50:
			rand = random.randrange(-50, 51)
			session['gold'] += rand
			if rand < 0:
				session['activities'].append(('Entered a ' + building + ' and lost ' + str(abs(rand)) + ' golds.. Ouch... (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'red'))
			elif rand >= 0:
				session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
		else:
			session['activities'].append(('You dont have enough golds to enter the casino. You must have at least 50. (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'red'))
			session.modified = True

	else:
		session['gold'] = 0
		session['activities'].append(('Cheaters never prosper. (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'red'))

	return redirect('/')

@app.route('/reset')
def reset():
	if session.get('gold') != None:
		session.pop('gold')

	if session.get('activities') != None:
		session.pop('activities')

	return redirect('/')

app.run(debug=True)