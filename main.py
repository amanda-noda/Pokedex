
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
label_id = Label(frame_pokemon, text='#94', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
label_id.place(x=10, y=70)

#Perfil Pokemon
image_perfil = Image.open('icone/gengar-94.png')
image_perfil = image_perfil.resize((230, 200))
image_perfil = ImageTk.PhotoImage(image_perfil)

label_image = Label(frame_pokemon, image=image_perfil,relief='flat', bg='white', fg='black')
label_image.place(x=80, y=50)
tipo_pok.lift()

##Status pokemon
status_pok = Label(janela, text='Status', relief='flat', anchor=CENTER, font=("Courier New",20), bg='white', fg='black')
status_pok.place(x=20, y= 300)
#HP
hp_pok = Label(janela, text='HP:60', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
hp_pok.place(x=20, y= 330)
#ataque
ataque_pok = Label(janela, text='Ataque:65', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
ataque_pok.place(x=20, y= 350)
#defesa
defesa_pok = Label(janela, text='Defesa:60', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
defesa_pok.place(x=20, y= 370)





janela.mainloop()
