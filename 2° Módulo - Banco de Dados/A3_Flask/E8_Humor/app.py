from flask import Flask, render_template

app = Flask(__name__)
image = True

@app.route('/')
def home():
    luffyBolado = 'https://i.pinimg.com/originals/50/c5/f1/50c5f1847013012ee0f25f67fdddb8d9.gif'

    return render_template(
    'index.html',
    luffyBolado = luffyBolado,
    image = image
    )

@app.route('/troca', methods = ['POST'])
def troca():
    image = False
    luffySuave = 'https://media.tenor.com/images/9ff03b679bf96782b7ff1fb4089ad7e9/tenor.gif'

    return render_template(
    'index.html',
    image = image,
    luffySuave = luffySuave,
    )

if __name__ == '__main__':
    app.run(debug = True)