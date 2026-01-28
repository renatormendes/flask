from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cria o arquivo 'database.db' na pasta do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Definir um modelo (tabela)
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(80), unique=True, nullable=False)

# Criar o banco e a tabela
with app.app_context():
	db.create_all()

@app.route('/')
def index():
	return "SQLIte Database Criado!"