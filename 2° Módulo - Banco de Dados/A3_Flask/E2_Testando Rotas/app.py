from flask import Flask

app = Flask (__name__)

@app.route('/')
def home():
    return 'Hellow Flask'

@app.route('/secondRoute')
def secondRoute():
    return '<h1> This page is referencied to second route</h1>'

@app.route('/Bluemer')
def bluemerRoute():
    return '<h1> Eu sou bluemer</h1>'

if __name__ == '__main__':
    app.run(debug=True)
