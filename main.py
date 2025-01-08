
from tkinter import *
from tkinter import ttk

#### cores ####
co0 = "444466" #Preto
co1 = "feffff" #Branco
co2 = "6f9fbd" #Azul
co3 = "38576b" #Valor
co4 = "403d3d" #Letra
co5 = "ef5350" #Vermelho

#Criando janela
janela = Tk()
janela.title('')
janela.geometry('1080x720')
#janela.configure (bg = co1)
#Oi

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")


janela.mainloop()
