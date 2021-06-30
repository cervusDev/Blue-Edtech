from flask import (Flask, render_template)
from flask_sqlalchemy import (SQLAlchemy)

#Inicialização do Flask
app = Flask(__name__)

# Configurando o banco de dados
user = 'xbjebcjp'
password = 'jgQSsvr7VQeW2k1nJbSxirnjNi0Dijhj'
host = 'tuffi.db.elephantsql.com'
database = 'xbjebcjp'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'adwaita'

#Inicialização do banco de dados
db = SQLAlchemy(app)

#Modelando o banco de dados
class Filmes(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  nome   = db.Column(db.String(255), nullable = False)
  url = db.Column(db.String(255), nullable = False)

  def __init__(self, nome, url):
    self.nome = nome
    self.url = url

  # Conversor de função para método: lendo todos os elementos
  @staticmethod
  def read_all():
    #select * from filmes order by id asc
    #query = select 
    return Filmes.query.order_by(Filmes.id.asc()).all()
  
  @staticmethod
  def resume(registro_id):
    #select * from filmes where id == xpto
    return Filmes.query.get(registro_id) # Este parâmetro registro_id está ligado ao parâmetro da função details


#Rotas
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
  image = ''
  registro = Filmes.resume(registro_id)
  print(registro)

  if registro_id == 1:

    image = 'https://br.web.img2.acsta.net/medias/nmedia/18/91/08/82/20128877.JPG'

  elif registro_id == 2:

    image = 'https://images-na.ssl-images-amazon.com/images/I/61gZbAKOU5L._AC_SX522_.jpg'

  elif registro_id == 3:

    image = 'https://upload.wikimedia.org/wikipedia/pt/9/94/Matrix_revolutions.jpg'

  return render_template(
    'resume.html',
    image = image,
    registro = registro
  ) 


if __name__ == '__main__':
  app.run(debug = True)    