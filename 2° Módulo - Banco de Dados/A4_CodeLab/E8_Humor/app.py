from flask import Flask, render_template

app = Flask(__name__)
image = True

@app.route('/')
def home():
    luffyBolado = 'https://i.pinimg.com/originals/50/c5/f1/50c5f1847013012ee0f25f67fdddb8d9.gif'
    nome = 'Nome: Monk D. Luffy'
    humor = 'Humor: Luffy está '
    return render_template(
    'index.html',
    luffyBolado = luffyBolado,
    image = image,
    nome = nome ,
    humor = humor
    )

@app.route('/troca', methods = ['POST'])
def troca():
    image = False
    luffySuave = 'https://i.pinimg.com/originals/02/0c/e7/020ce7e3b883d974e73d9fdffb4f20ad.gif'
    nome = 'Nome: Monk D. Luffy'
    humor = 'Humor: Luffy está '
    return render_template(
    'index.html',
    image = image,
    luffySuave = luffySuave,
    nome = nome ,
    humor = humor
    )

if __name__ == '__main__':
    app.run(debug = True)