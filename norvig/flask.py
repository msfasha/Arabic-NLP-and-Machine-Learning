from flask import Flask
from norvig import *

app = Flask(__name__)

@app.route('/')
def home():
    return '<H1>Hello from Arabic Spell Checker</H1>'

@app.route('/check/<word>')
def check_word(word):
    return 'Most probable word is %s' % correction(word)

if __name__ == '__main__':
    app.run()