
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

##Cria a janela
janela = Tk()
janela.title('')
janela.geometry('960x660')
janela.configure(bg='white')

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=600)

style = ttk.Style(janela)
style.theme_use("clam")

##Cria Frame
frame_pokemon = Frame(janela, width=1200, height=290, relief='flat')
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
#ataque especial
sp_ataque_pok = Label(janela, text='Ataque especial:130', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
sp_ataque_pok.place(x=20, y= 370)
#defesa
defesa_pok = Label(janela, text='Defesa:60', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
defesa_pok.place(x=20, y= 390)
#defesa especial
sp_defesa_pok = Label(janela, text='Defesa especial:75', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
sp_defesa_pok.place(x=20, y= 410)
#velocidade
velocidade_pok = Label(janela, text='Velocidade:110', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
velocidade_pok.place(x=20, y= 430)
#total
total_pok = Label(janela, text='Total:500', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
total_pok.place(x=20, y= 450)

##Habilidades pokemon
Habilidade_pok = Label(janela, text='Habilidade', relief='flat', anchor=CENTER, font=("Courier New",20), bg='white', fg='black')
Habilidade_pok.place(x=300, y= 300)

HB1_pok = Label(janela, text='Raio da Confusão', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
HB1_pok.place(x=300, y= 330)

HB2_pok = Label(janela, text='Soco das Sombras', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
HB2_pok.place(x=300, y= 350)

HB3_pok = Label(janela, text='Bola das Sombras', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
HB3_pok.place(x=300, y= 370)

HB4_pok = Label(janela, text='Vibração Sombria', relief='flat', anchor=CENTER, font=("Courier New",10), bg='white', fg='black')
HB4_pok.place(x=300, y= 390)

##cria Botoes

#Botão 1
image_perfil_1 = Image.open('icone/gengar-94.png')
image_perfil_1 = image_perfil_1.resize((40,40))
image_perfil_1 = ImageTk.PhotoImage(image_perfil_1)

b_pok_1 = Button(janela, image=image_perfil_1, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_1.place(x=380, y=10)

#Botão 2
image_perfil_2 = Image.open('icone/aerodactyl-142.png')
image_perfil_2 = image_perfil_2.resize((40,40))
image_perfil_2 = ImageTk.PhotoImage(image_perfil_2)

b_pok_2 = Button(janela, image=image_perfil_2, text='Aerodactyl', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_2.place(x=380, y=60)

#Botão 3
image_perfil_3 = Image.open('icone/bulbasaur-001.png')
image_perfil_3 = image_perfil_3.resize((40,40))
image_perfil_3 = ImageTk.PhotoImage(image_perfil_3)

b_pok_3 = Button(janela, image=image_perfil_3, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_3.place(x=380, y=110)

#Botão 4
image_perfil_4 = Image.open('icone/charmander-004.png')
image_perfil_4 = image_perfil_4.resize((40,40))
image_perfil_4 = ImageTk.PhotoImage(image_perfil_4)

b_pok_4 = Button(janela, image=image_perfil_4, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_4.place(x=380, y=160)

#Botão 5
image_perfil_5 = Image.open('icone/crobat-169.png')
image_perfil_5 = image_perfil_5.resize((40,40))
image_perfil_5 = ImageTk.PhotoImage(image_perfil_5)

b_pok_5 = Button(janela, image=image_perfil_5, text='Crobat', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_5.place(x=380, y=210)

#Botão 6
image_perfil_6 = Image.open('icone/cubone-104.png')
image_perfil_6 = image_perfil_6.resize((40,40))
image_perfil_6 = ImageTk.PhotoImage(image_perfil_6)

b_pok_6 = Button(janela, image=image_perfil_6, text='Cubone', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_6.place(x=550, y=10)

#Botão 7
image_perfil_7 = Image.open('icone/mew-151.png')
image_perfil_7 = image_perfil_7.resize((40,40))
image_perfil_7 = ImageTk.PhotoImage(image_perfil_7)

b_pok_7 = Button(janela, image=image_perfil_7, text='Mew', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_7.place(x=550, y=60)

#Botão 1
image_perfil_8 = Image.open('icone/mewtwo-150.png')
image_perfil_8 = image_perfil_8.resize((40,40))
image_perfil_8 = ImageTk.PhotoImage(image_perfil_8)

b_pok_8 = Button(janela, image=image_perfil_8, text='Mewtwo', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_8.place(x=550, y=110)

#Botão 9
image_perfil_9 = Image.open('icone/pikachu-25.png')
image_perfil_9 = image_perfil_9.resize((40,40))
image_perfil_9 = ImageTk.PhotoImage(image_perfil_9)

b_pok_9 = Button(janela, image=image_perfil_9, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_9.place(x=550, y=160)

#Botão 10
image_perfil_10 = Image.open('icone/squitle-007.png')
image_perfil_10 = image_perfil_10.resize((40,40))
image_perfil_10 = ImageTk.PhotoImage(image_perfil_10)

b_pok_10 = Button(janela, image=image_perfil_10, text='Squitle', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_10.place(x=550, y=210)

#Botão 11
image_perfil_11 = Image.open('icone/umbreon-197.png')
image_perfil_11 = image_perfil_11.resize((40,40))
image_perfil_11 = ImageTk.PhotoImage(image_perfil_11)

b_pok_11 = Button(janela, image=image_perfil_11, text='Umbreon', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_11.place(x=720, y=10)

#Botão 12
image_perfil_12 = Image.open('icone/vaporeon-134.png')
image_perfil_12 = image_perfil_12.resize((40,40))
image_perfil_12= ImageTk.PhotoImage(image_perfil_12)

b_pok_12 = Button(janela, image=image_perfil_12, text='Vaporeon', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_12.place(x=720, y=60)

#Botão 13
image_perfil_13 = Image.open('icone/hypno-097.png')
image_perfil_13 = image_perfil_13.resize((40,40))
image_perfil_13= ImageTk.PhotoImage(image_perfil_13)

b_pok_13 = Button(janela, image=image_perfil_13, text='Hypno', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_13.place(x=720, y=110)

#Botão 14
image_perfil_14 = Image.open('icone/lapras-131.png')
image_perfil_14 = image_perfil_14.resize((40,40))
image_perfil_14 = ImageTk.PhotoImage(image_perfil_14)

b_pok_14 = Button(janela, image=image_perfil_14, text='Lapras', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Courier New", 12), bg='white', fg='black')
b_pok_14.place(x=720, y=160)

#Botão 15
image_perfil_15 = Image.open('icone/scyther-123.png')
image_perfil_15 = image_perfil_15.resize((40,40))
image_perfil_15 = ImageTk.PhotoImage(image_perfil_15)

b_pok_15 = Button(janela, image=image_perfil_15, text='Scyther', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, ancho=NW, padx=5, font=("Courier new", 12), bg='white', fg='black')
b_pok_15.place(x=720, y=210)

janela.mainloop()