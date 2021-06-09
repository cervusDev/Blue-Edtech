from flask import Flask

#Inicializar o objeto Flask
app = Flask (__name__)

#Iniciar e declarar a rota da home page com o elemento "barra" ('/')
@app.route("/")

def home():
    return 'Primeiro exemplo com flask'

if __name__ == '__main__':
    app.run (debug = True)