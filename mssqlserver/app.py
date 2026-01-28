from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)

# params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=master;UID=sa;PWD=MasterKey123#$")
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"

# Cria o banco de dados database no servidor mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:MasterKey123#$@127.0.0.1:1433/master?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)

# Definir um modelo (tabela)
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(80), unique = True, nullable = False)

# Criar o banco e a tabela
with app.app_context():
	db.create_all()

@app.route('/')
def index():
	return "SQLite Database Criado!"
