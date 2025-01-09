
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk


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
label_pokemon.place(x=10, y=15)

##Tipo pokemon
tipo_pok = Label(frame_pokemon, text='Fantasma', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black' )
tipo_pok.place(x=10, y= 50)

#Cria Id
label_id = Label(frame_pokemon, text='#', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
label_id.place(x=10, y=70)

#Perfil Pokemon
image = Image.open('icone/094.png')
image = image.resize((238,238))
image = ImageTk.PhotoImage(image)

label_image = Label(frame_pokemon, image=image,relief='flat', bg='white', fg='black')
label_image.place(x=10, y=100)



janela.mainloop()
