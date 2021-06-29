from flask import (Flask, Blueprint, render_template)

app = Flask(__name__)

registros = [
  {
    'id': 1,
    'nome': 'Matrix',
    'url':'https://br.web.img2.acsta.net/medias/nmedia/18/91/08/82/20128877.JPG'
  },
  {
    'id': 2,
    'nome': 'Matrix Reloaded',
    'url':'https://images-na.ssl-images-amazon.com/images/I/61gZbAKOU5L._AC_SX522_.jpg'
  },
  {
    'id': 3,
    'nome': 'Matrix Revolution',
    'url':'https://upload.wikimedia.org/wikipedia/pt/9/94/Matrix_revolutions.jpg'
  }
]

@app.route('/')
def home ():
  return render_template(
    'main.html',

  )

@app.route('/read')
def read ():
  return render_template(
    'read.html',
    registros = registros
  )

@app.route('/read/<registro_id>')
def details (registro_id):
  return 'pagina do filme' + registro_id


# trabalhar com dados mockados

if __name__ == '__main__':
  app.run(debug = True)    