import sqlite3 as lite


#Criando conexão
con = lite.connect('dados.db')

#Create Table
#with abre e fecha o banco de dados.
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE lista_tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100))")
    