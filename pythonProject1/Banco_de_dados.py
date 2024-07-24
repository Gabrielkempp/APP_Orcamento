import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Função para criar tabelas
def criar_tabelas():
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")
        cur.execute("CREATE TABLE IF NOT EXISTS Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")

# Chamada para criar as tabelas quando o módulo é importado
criar_tabelas()