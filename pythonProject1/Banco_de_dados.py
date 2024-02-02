#Importando SQLite
import sqlite3 as lite

#Crando conexao
con = lite.connect('dados.db')

#Criando tabela de categorias
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(ID INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

#Criando tabela de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(ID INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

#Criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(ID INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")