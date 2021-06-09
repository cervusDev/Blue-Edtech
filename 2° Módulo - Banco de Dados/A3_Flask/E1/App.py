from flask import Flask

#Inicializar o objeto Flask
app = Flask (__name__)

#Iniciar e declarar a rota da home page com o elemento "barra" ('/')
@app.route("/")

def home():
    return 'Hellow Blue'