from tkinter import * #tambem pode usar "import tkinter"
from tkinter import Tk, ttk

#importando pillow
from PIL import Image, ImageTk

# Importando barra de progresso
from tkinter.ttk import Progressbar

# Importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Importando Calendario
from tkcalendar import Calendar, DateEntry
from datetime import date

#Cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"
co10 = "#22262b" #0D1117"
co11 = "#383b41" #Background

colors = ['#2ecc71', '#e74c3c','#3498db', '#ee9944', '#444466', '#bb5555']
#colors = Verde, Vermelho, Azul

#Criando Janela
janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co10)#projeto-inicial-era-#e9edf5
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")


#Criando blocos para dividir a tela
frameCima = Frame(janela, width=1043, height=50, background=co11, relief= "flat")
frameCima.grid(row=0, column=0, padx=1)

frameMeio = Frame(janela, width=1043, height=325, background=co11, pady=20, relief= "raised")
frameMeio.grid(row=1, column=0, pady=2, padx= 1, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=270, background=co11, relief= "flat")
frameBaixo.grid(row=2, column=0, pady=0, padx= 1, sticky=NSEW)

frame_gra_pie = Frame(frameMeio, width=580, height=250, background=co11)
frame_gra_pie.place(x=415, y=5)


#Trabalhando no frame de Cima

#acessando imagem
app_img = Image.open('coin.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image = app_img, text = "  The Wallet", width=250, compound = LEFT, padx = 5 , anchor= NW, font=("Verdana 20 bold"),bg= co11, fg=co1)
app_logo.place(x=315, y=0)

# Percentagem ---------------------------------------------------------------
def percentagem():
    l_nome = Label(frameMeio, text='Porcentagem da Receita Gasta', height= 1, anchor=NW, font= ('Verdana 12 bold'), bg=co11, fg=co1)
    l_nome.place(x=10, y=-10)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('black.Horizontal.TProgressbar', background= "#2ecc71")
    style.configure("TProgressbar", thickness= 15)

    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')

    bar.place(x=15, y=20)
    bar['value'] = 50

    valor=50

    l_percentagem = Label(frameMeio, text='{:,.2f}%'.format(valor), anchor=NW, font=('Verdana 12 bold'), bg=co11, fg=co1)
    l_percentagem.place(x=200, y=17)


# Função para gráfico de barras ---------------------------
def grafico_bar():
    lista_categorias = ['Renda', 'Despesa', 'Saldo']
    lista_valores = [3000, 2000, 6223]

    figura, ax = plt.subplots(figsize=(4, 3.45), dpi=60)
    figura.patch.set_facecolor(co11)

    barras = ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

    for i, barra in enumerate(barras):
        ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.5,
                str("{:,.0f}".format(lista_valores[i])),
                fontsize=17, fontstyle='italic', ha='center', va='bottom', color='white')

    # Configurações do eixo X
    ax.set_xticks(range(len(lista_categorias)))
    ax.set_xticklabels(lista_categorias, fontsize=16)

    # Configurações do eixo Y
    ax.yaxis.grid(False)

    ax.patch.set_facecolor(co11)

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Configurações das bordas
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('white')
        ax.spines[spine].set_linewidth(1)

    for spine in ['right', 'top']:
        ax.spines[spine].set_color(co11)
        ax.spines[spine].set_linewidth(1)


    ax.spines['bottom'].set_color('#CCCCCC')

    # Configurações adicionais
    ax.set_axisbelow(True)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=20, y=80)


#Função de Resumo total
def resumo():
    valor = [500, 600, 420]

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor= NW, font=('Arial 1'), bg=co1)
    l_linha.place(x=309, y=62)
    l_sumario = Label(frameMeio, text="Total Da Renda Mensal      ", anchor=NW, font=('Verdana 12 bold'), bg=co11, fg=colors[0])
    l_sumario.place(x=309, y=45)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co11, fg=co1)
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg=co1)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total De Gasto Mensal    ", anchor=NW, font=('Verdana 12 bold'), bg=co11,fg=colors[1])
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co11, fg=co1)
    l_sumario.place(x=309, y=150)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg=co1)
    l_linha.place(x=309, y=217)
    l_sumario = Label(frameMeio, text="Total Saldo Em Caixa       ", anchor=NW, font=('Verdana 12 bold'), bg=co11,fg=colors[2])
    l_sumario.place(x=309, y=200)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co11, fg=co1)
    l_sumario.place(x=309, y=230)

#Função Grafico Pie
def grafico_pie():
    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90, facecolor=co11)
    ax = figura.add_subplot(111)

    lista_valores = [345, 225, 534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    #only "explode" the 2nd slice(i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,
               shadow=False, startangle=90, textprops={'color': 'white'})
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.45, 0.20))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=10, column=20, padx=20, pady=0)

percentagem()
grafico_bar()
resumo()
grafico_pie()

#Criando frames dentro do frameBaixo
frameRenda = Frame(frameBaixo, width=300, height=270, background=co11)
frameRenda.grid(row=0, column=0)

frameOperacoes = Frame(frameBaixo, width=220, height=270, background=co11)
frameOperacoes.grid(row=0, column=1, padx=25, pady=15)

frameConfiguracao = Frame(frameBaixo, width=220, height=270, background=co11)
frameConfiguracao.grid(row=0, column=2, padx=25, pady=15)

#Tabela Renda Mensal------------------------------------------------
app_tabela = Label(frameBaixo, text = "Tabela Receitas e Despesas", anchor= NW, font=("Verdana 12 bold"),bg= co11, fg=co1)
app_tabela.place(x=45, y=0)

#Função para mostrar_renda
def mostrar_renda():

    tabela_head = ['#Id', 'Categoria', 'Data', 'Quantidade']

    lista_itens = [[0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4]]

    global tree

    tree = ttk.Treeview(frameRenda, selectmode="extended", columns=tabela_head, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frameRenda, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameRenda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    frameRenda.grid(pady=(12, 0), padx=(5, 0))

    tree.grid(column=0, row=0, pady=0, padx=0, sticky='nsew')
    vsb.grid(column=1, row=0, padx= 0, pady=0, sticky='ns')
    hsb.grid(column=0, row=1, padx=0,sticky='ew')

    hd = ["center", "center", "center", "center"]
    h = [30, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        #adjust the column 's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostrar_renda()

#Configurações Despesas-----------
l_info = Label(frameOperacoes, text='Insira Novas Despesas', height='1', anchor=NW, font=('Verdana 12 bold'), bg=co11, fg=co1)
l_info.place(x=10, y=0)

#Categoria-------------------------
l_Categoria = Label(frameOperacoes, text='Categoria', height='1', anchor=NW, font=('Ivy 10 bold'), bg=co11, fg=co1)
l_Categoria.place(x=10, y=30)

#Adicionando categorias------------
categoria_funcao = ['Viagem', 'Comida']
categoria = []

for i in categoria_funcao:
    categoria.append(i[1])
combo_categoria_despesas = ttk.Combobox(frameOperacoes, width= 10, font=('Ivy 10'))
combo_categoria_despesas['values'] = (categoria)
combo_categoria_despesas.place(x=120, y=31)


#Configurações Despesas-------------------------------------------------------------------------------------------------
l_cal_Despesas = Label(frameOperacoes, text='Data', height='1', anchor=NW, font=('Ivy 10 bold'), bg=co11, fg=co1)
l_cal_Despesas.place(x=10, y=60)
e_cal_Despesas = DateEntry(frameOperacoes, width=12, background='#4b4f57', foreground=co1, borderwidth=2, year=2024)
e_cal_Despesas.place(x=120, y=61)

#Valor
l_valor_Despesas = Label(frameOperacoes, text='Valor Total R$', height='1', anchor=NW, font=('Ivy 10 bold'), bg=co11, fg=co1)
l_valor_Despesas.place(x=10, y=90)
e_valor_Despesas = Entry(frameOperacoes, width=14, justify='left', relief='solid')
e_valor_Despesas.place(x=120, y=91)

#Botão inserir
img_add_despesas = Image.open('plus.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)
botao_inserir_despesas = Button(frameOperacoes, image = img_add_despesas, text = "Adicionar".upper(), width=80, compound = LEFT, anchor= NW, font=("Ivy 7 bold"),bg= co11, fg=co1, overrelief=SUNKEN)
botao_inserir_despesas.place(x=120, y=121)

#Botão Excluir
l_excluir_cat = Label(frameOperacoes, text='Excluir Ação', height='1', anchor=NW, font=('Ivy 10 bold'), bg=co11, fg=co1)
l_excluir_cat.place(x=10, y=190)
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((17,17))
img_delete = ImageTk.PhotoImage(img_delete)
botao_delete = Button(frameOperacoes, image = img_delete, text = "Excluir".upper(), width=80, compound = LEFT, anchor= NW, font=("Ivy 7 bold"),bg= co11, fg=co1, overrelief=SUNKEN)
botao_delete.place(x=120, y=190)

#Configurações Receitas-------------------------------------------------------------------------------------------------
l_info = Label(frameConfiguracao, text='Insira Novas Receitas', height='1', anchor=NW, font=('Verdana 12 bold'), bg=co11, fg=co1)
l_info.place(x=10, y=0)

#Calendario Receitas
l_cal_Receitas = Label(frameConfiguracao, text='Data', height='1', anchor=NW, font=('Ivy 10 bold'), bg=co11, fg=co1)
l_cal_Receitas.place(x=10, y=30)
e_cal_Receitas = DateEntry(frameConfiguracao, width=12, background='#4b4f57', foreground=co1, borderwidth=2, year=2024)
e_cal_Receitas.place(x=120, y=31)

#Valor (Receitas)
l_valor_Receitas = Label(frameConfiguracao, text='Valor Total R$', height='1', anchor=NW, font=('Ivy 10 bold'), bg=co11, fg=co1)
l_valor_Receitas.place(x=10, y=60)
e_valor_Receitas = Entry(frameConfiguracao, width=14, justify='left', relief='solid')
e_valor_Receitas.place(x=120, y=61)

#Botão inserir
img_add_receitas = Image.open('plus.png')
img_add_receitas = img_add_receitas.resize((17,17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)
botao_inserir_despesas = Button(frameConfiguracao, image = img_add_receitas, text = "Adicionar".upper(), width=80, compound = LEFT, anchor= NW, font=("Ivy 7 bold"),bg= co11, fg=co1, overrelief=SUNKEN)
botao_inserir_despesas.place(x=120, y=91)

#Configurações Nova Categoria-------------------------------------------------------------------------------------------
l_info = Label(frameConfiguracao, text='Nova Categoria', height='1', anchor=NW, font=('Verdana 12 bold'), bg=co11, fg=co1)
l_info.place(x=10, y=157)
e_nome_categoria = Entry(frameConfiguracao, width=14, justify='left', relief='solid')
e_nome_categoria.place(x=15, y=193)

#Botão inserir
img_add_categoria = Image.open('plus.png')
img_add_categoria = img_add_categoria.resize((17,17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
botao_inserir_despesas = Button(frameConfiguracao, image = img_add_categoria, text = "Adicionar".upper(), width=80, compound = LEFT, anchor= NW, font=("Ivy 7 bold"),bg= co11, fg=co1, overrelief=SUNKEN)
botao_inserir_despesas.place(x=120, y=190)


janela.mainloop()