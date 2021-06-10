from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():

    player = 'Monk D. '
    award = False

    return render_template(
    'index.html',
    player = player,
    award = award,
    )

if __name__ == '__main__':
    app.run(debug = True)