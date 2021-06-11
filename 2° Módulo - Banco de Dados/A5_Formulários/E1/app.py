from os import name
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        social = request.form['social-midia']
        socialtwo = request.form['social-two']
        socialthree = request.form['social-three']

        print(f'User Name: {name}')
        print(f'Your Password: {password}')
        print(f'Social Media: {social}')
        print(f'Social Media: {socialtwo}')
        print(f'Social Media: {socialthree}')

    return render_template(
    'index.html',
    )

if __name__ == '__main__':
    app.run(debug = True)