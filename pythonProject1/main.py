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

#Cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"
co10 = "#22262b" #0D1117"
co11 = "#383b41"

colors = ['#2ecc71', '#e74c3c','#3498db', '#ee9944', '#444466', '#bb5555']

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

frameMeio = Frame(janela, width=1043, height=361, background=co11, pady=20, relief= "raised")
frameMeio.grid(row=1, column=0, pady=2, padx= 1, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, background=co11, relief= "flat")
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

'''#Função para grafico bar ---------------------------
def percentagem():
    l_nome = Label(frameMeio, text='Porcentagem da Receita Gasta', height=1, anchor=NW, font=('Verdana 12 bold'), bg=co11, fg=co1)
    l_nome.place(x=10, y=-10)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('black.Horizontal.TProgressbar', background="#2ecc71")
    style.configure("TProgressbar", thickness=15)

    bar = Progressbar(frameMeio, length=200, style='black.Horizontal.TProgressbar', value=50)
    bar.place(x=15, y=20)

    l_percentagem = Label(frameMeio, text='{:,.2f}%'.format(bar['value']), anchor=NW, font=('Verdana 12 bold'), bg=co11, fg=co1)
    l_percentagem.place(x=220, y=17)'''

# Função para gráfico de barras ---------------------------
def grafico_bar():
    lista_categorias = ['Renda', 'Despesa', 'Saldo']
    lista_valores = [3000, 2000, 6223]

    figura, ax = plt.subplots(figsize=(4, 3.45), dpi=60)
    figura.patch.set_facecolor('#383b41')

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

    ax.patch.set_facecolor('#383b41')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Configurações das bordas
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('white')
        ax.spines[spine].set_linewidth(1)

    for spine in ['right', 'top']:
        ax.spines[spine].set_color('#383b41')
        ax.spines[spine].set_linewidth(1)


    ax.spines['bottom'].set_color('#CCCCCC')

    # Configurações adicionais
    ax.set_axisbelow(True)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)


#Função de Resumo total
def resumo():
    valor = [500, 600, 420]

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor= NW, font=('Arial 1'), bg=co1)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total Da Renda Mensal      ", anchor=NW, font=('Verdana 12 bold'), bg=co11, fg="#2ecc71")
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co11, fg=co1)
    l_sumario.place(x=309, y=60)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg=co1)
    l_linha.place(x=309, y=122)
    l_sumario = Label(frameMeio, text="Total De Gasto Mensal    ", anchor=NW, font=('Verdana 12 bold'), bg=co11,fg="#e74c3c")
    l_sumario.place(x=309, y=105)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co11, fg=co1)
    l_sumario.place(x=309, y=140)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg=co1)
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Total Saldo Em Caixa       ", anchor=NW, font=('Verdana 12 bold'), bg=co11,fg="#3498db")
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co11, fg=co1)
    l_sumario.place(x=309, y=220)

#Função Grafico Pie
def grafico_pie():
    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90, facecolor='#383b41')
    ax = figura.add_subplot(111)

    lista_valores = [345, 225, 534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    #only "explode" the 2nd slice(i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,
               shadow=False, startangle=90, textprops={'color': 'white'})
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.50, 0.20))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=20, column=20, padx=20, pady=20)




percentagem()
grafico_bar()
resumo()
grafico_pie()
janela.mainloop()