import pyodbc
from flask import Flask

app = Flask(__name__)

server = 'GABRIEL-PC\SQLEXPRESS'
database = 'ESTUDO'
username = 'gabriel'
password = '123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

nome = "Gabrielo Cordeiro"
filhos = 1
data = "2007-02-21"


@app.route('/insert', methods=["POST"])
def inst():
    comando = f"insert into pessoa values (next value for sq_pessoa, '{nome}', {filhos}, '{data}');"
    cursor.execute(comando)
    cursor.commit()
    return "Feito"


app.run(host='0.0.0.0')