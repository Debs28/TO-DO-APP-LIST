from ctypes import Union
import sqlite3 as lite

con = lite.connect('dados.db')


#Inserir informações (create)
def create_to_do(dado):
    with con:
        cur = con.cursor()
        query = "INSERT INTO lista_tarefas (nome) VALUES (?)"
        cur.execute(query,dado)

def update_to_do(dado):
     with con:
        cur = con.cursor()
        query = "UPDATE lista_tarefas SET nome=? WHERE id=?"
        cur.execute(query,dado)



def listar_to_do():
    with con:
        lista_tarefas = []
        cur = con.cursor()
        query = "SELECT * FROM lista_tarefas"
        cur.execute(query)
        info = cur.fetchall()
        for tarefa in info:
            lista_tarefas.append(tarefa)
            
    return lista_tarefas

def delete_to_do(dado):
    with con:
        cur = con.cursor()
        query = "DELETE FROM lista_tarefas WHERE id=?"
        cur.execute(query, dado)

def delete_all():
    with con:
        cur = con.cursor()
        query = "DELETE FROM lista_tarefas"
        cur.execute(query)