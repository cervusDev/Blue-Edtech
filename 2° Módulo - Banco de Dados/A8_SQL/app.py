from flask import (Flask, render_template)
from flask_sqlalchemy import (SQLAlchemy)

app = Flask(__name__)

#DataBase constructor
user = 'xbjebcjp'
password = 'jgQSsvr7VQeW2k1nJbSxirnjNi0Dijhj'
host = 'tuffi.db.elephantsql.com'
database = 'xbjebcjp'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'adwaita'

db = SQLAlchemy(app)

#Filmes

class Filmes(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(255), nullable = False)
  url = db.Column(db.String(255), nullable = False)

  def __init__(self, nome, url):
    self.nome = nome
    self.url = url
  
  @staticmethod
  def read_all():
    return Filmes.query.order_by(Filmes.id.desc()).all()

@app.route('/')
def home ():
  return render_template(
    'main.html',

  )

@app.route('/read')
def read ():
  registros = Filmes.read_all()
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