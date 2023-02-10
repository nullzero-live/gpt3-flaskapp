from flask import Flask
from flask import Flask, render_template, request
from datetime import date
import os
import openai, aicontent
import json
import requests
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()

#Set openAI key
def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

#OpenAI key info
KEY_NAME = os.getenv("OPENAI_KEY")
set_openai_key(KEY_NAME)


#Defining route and function
#it can be extened, depending upon your choice, See Open AI example below for more details



@app.route('/')
def hello_world():
    return render_template('index.html')

#new route for new.html

@app.route('/new', methods=["GET", "POST"])
def new():
    if request.method == 'POST':
        query = request.form['Description']
        temp = request.form['temp']
        temp = float(temp)
        length = request.form['length']
        length = int(length)
        tp = request.form['tp']
        tp = float(tp)
        freq = request.form['freq']
        freq = float(freq)
        presence = request.form['presence']
        presence = float(presence)
        bo = request.form['bo']
        bo = int(bo)
        eng = 'text-davinci-003'
        openAIAnswer = aicontent.openAIQuery(eng,query,temp,length,tp,freq,presence,bo)
    return render_template('new.html', **locals())