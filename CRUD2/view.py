#importando sqlite

import sqlite3 as lite

#criando conexão

con = lite.connect('bd.bd')

lista = []

#inserindo informações

def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, data) VALUES (?, ?, ?, ?)"
        cur.execute(query,i)

#acessar informações

def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista

#atualizar informações

def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, data=? WHERE ID=?"
        cur.execute(query,i)


#deletar informações 

def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE ID=?"
        cur.execute(query,i)

