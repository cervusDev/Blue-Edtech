from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    luffy_name = 'Monkey D. Luffy'
    kaido_name = 'Kaido das Feras'

    exibir_imagem = True

    luffy = 'https://i.pinimg.com/originals/17/dc/31/17dc31b25944a72c94ef40bd121dd66c.gif'
    kaido = 'https://i.pinimg.com/originals/48/79/f5/4879f5159b4905d90f03bf591e16b074.gif'
    
    return render_template(
    'index.html',
    exibir_imagem = exibir_imagem,
    luffy_name = luffy_name,
    luffy = luffy,
    kaido = kaido,
    )

if __name__ == '__main__':
    app.run(debug = True)