#Importando SQLite
import sqlite3 as lite

import pandas as pd

#Crando conexao
con = lite.connect('dados.db')

#Funçoes de inserção-------------------------------------------------
#Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

#Inserir receitas
def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

#Inserir gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)


#Funçoes para deletar-------------------------------------------------

#Deletar Receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

#Deletar Gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)

#Funçoes para ver dados-------------------------------------------------

#ver Categorias
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#ver Receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#ver Gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Função para dados da tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista


# Função para dados do grafico barra
def bar_valores():
    # Receita total ---------------------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesa total ---------------------------------------
    despesa = ver_gastos()
    despesa_lista = []

    for i in despesa:
        despesa_lista.append(i[3])

    despesa_total = sum(despesa_lista)

    # Saldo total ---------------------------------------
    saldo_total = receita_total - despesa_total

    return [receita_total, despesa_total, saldo_total]

# Função Grafico Pie
def pie_valores():
    gastos = ver_gastos()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns = ['id', 'Categoria', 'Data', 'Valor'])
    dataframe = dataframe.groupby('Categoria')['Valor'].sum()

    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return ([lista_categorias,lista_quantias])

def porcentagem_valor():
    # Receita Total ---------------------------------------
    receitas = ver_receitas()
    receitas_lista = []

    if receitas:
        for i in receitas:
            receitas_lista.append(i[3])
        receita_total = sum(receitas_lista)
    else: receita_total = 0

    # Despesa Total ---------------------------------------
    despesa = ver_gastos()
    despesa_lista = []

    if despesa:
        for i in despesa:
            despesa_lista.append(i[3])
        despesa_total = sum(despesa_lista)
    else: despesa_total = 0

    # Total gasto % ---------------------------------------
    if receita_total == 0:
        total_gasto = 0
    else:
        total_gasto = (despesa_total/receita_total)*100
        if total_gasto > 100:
            total_gasto = 100

    return [total_gasto]