#importando sqlite

import sqlite3 as lite

#criando conexão

con = lite.connect('bd.bd')

#criando tabela 

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, data TEXT)")

    

