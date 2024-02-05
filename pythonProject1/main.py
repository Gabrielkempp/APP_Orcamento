from tkinter import * #tambem pode usar "import tkinter"
from tkinter import Tk, ttk

#importando pillow
from PIL import Image, ImageTk

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

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

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


#Trabalhando no frame de Cima

#acessando imagem
app_img = Image.open('coin.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image = app_img, text = "  The Wallet", width=250, compound = LEFT, padx = 5 , anchor= NW, font=("Verdana 20 bold"),bg= co11, fg=co1)
app_logo.place(x=315, y=0)



janela.mainloop()