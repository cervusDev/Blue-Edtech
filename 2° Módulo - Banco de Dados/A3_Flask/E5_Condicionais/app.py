from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Badass Sonic'
    hp = 2000
    
    exibir_imagem = True
    imagem = 'https://i.pinimg.com/originals/82/81/4e/82814e4a976d84271a133821984bdc87.png'
    
    return render_template(
    'index.html',
    name = name,
    hp = hp,
    exibir_imagem = exibir_imagem,
    imagem = imagem
    )

if __name__ == '__main__':
    app.run(debug = True)