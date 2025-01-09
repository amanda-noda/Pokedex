
from tkinter import *
from tkinter import ttk



##Cria a janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg='white')

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

##Cria Frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

#Cria Label
label_pokemon = Label(frame_pokemon, text='Gengar', relief='flat', anchor=CENTER, font=("Courier New",20), bg='white', fg='black')
label_pokemon.place(x=10,y=15)

##Tipo pokemon
tipo_pok = Label(frame_pokemon, text='Fantasma', relief='flat', anchor=CENTER, font=('Fixedsys 12'), bg='white', fg='black' )
tipo_pok.place(x=10, y= 15)

#Cria Id
label_id = Label(frame_pokemon, text='#', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
label_id.place(x=10,y=50)



janela.mainloop()
