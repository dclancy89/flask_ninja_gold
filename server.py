import random
from flask import Flask, render_template, request, redirect, session, Markup
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


app.run(debug=True)