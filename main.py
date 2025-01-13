
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from dados import *

# Cria a janela
janela = Tk()
janela.title('')
janela.geometry('960x660')
janela.configure(bg='white')

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=600)

style = ttk.Style(janela)
style.theme_use("clam")


def trocar_pokemon(i):
    global image_perfil, label_image, frame_pokemon

    # trocar pokemon
    label_pokemon['text'] = i
    label_pokemon['bg'] = pokemon[i]['tipo'][3]
    label_id['text'] = pokemon[i]['tipo'][0]
    label_id['bg'] = pokemon[i]['tipo'][3]
    tipo_pok['text'] = pokemon[i]['tipo'][1]
    tipo_pok['bg'] = pokemon[i]['tipo'][3]

    frame_pokemon['bg'] = pokemon[i]['tipo'][3]
    image_perfil = pokemon[i]['tipo'][2]

    # Perfil Pokemon
    image_perfil = Image.open(image_perfil)
    image_perfil = image_perfil.resize((230, 200))
    image_perfil = ImageTk.PhotoImage(image_perfil)

    label_image = Label(frame_pokemon, image=image_perfil,
                        relief='flat', bg=pokemon[i]['tipo'][3], fg='black')
    label_image.place(x=80, y=50)
    tipo_pok.lift()

    # trocar status
    hp_pok['text'] = pokemon[i]['status'][0]
    ataque_pok['text'] = pokemon[i]['status'][1]
    sp_ataque_pok['text'] = pokemon[i]['status'][2]
    defesa_pok['text'] = pokemon[i]['status'][3]
    sp_defesa_pok['text'] = pokemon[i]['status'][4]
    velocidade_pok['text'] = pokemon[i]['status'][5]
    total_pok['text'] = pokemon[i]['status'][6]

    # trocar habilidade
    HB1_pok['text'] = pokemon[i]['habilidade'][0]
    HB2_pok['text'] = pokemon[i]['habilidade'][1]
    HB3_pok['text'] = pokemon[i]['habilidade'][2]
    HB4_pok['text'] = pokemon[i]['habilidade'][3]

    # trocar descrição
    descricao_pok1['text'] = pokemon[i]['descricao'][0]


# Cria Frame
frame_pokemon = Frame(janela, width=1200, height=290,
                      relief='flat', bg='#1992fc')
frame_pokemon.grid(row=1, column=0)

# Cria Label
label_pokemon = Label(frame_pokemon, text='Pokedex', relief='flat',
                      anchor=CENTER, font=("Fixedsys", 27), bg='#1992fc', fg='white')
label_pokemon.place(x=10, y=2)

# Tipo pokemon
tipo_pok = Label(frame_pokemon, text='Tipo', relief='flat', anchor=CENTER, font=(
    "Poppins 10 bold"), bg='#1992fc', fg='white')
tipo_pok.place(x=10, y=50)

# Cria Id
label_id = Label(frame_pokemon, text='ID', relief='flat', anchor=CENTER, font=(
    "Poppins 10 bold"), bg='#1992fc', fg='white')
label_id.place(x=10, y=70)

image_perfil = Image.open('icone/pokebola.png')
image_perfil = image_perfil.resize((230, 200))
image_perfil = ImageTk.PhotoImage(image_perfil)

label_image = Label(frame_pokemon, image=image_perfil,
                    relief='flat', bg='#1992fc', fg='black')
label_image.place(x=80, y=50)
tipo_pok.lift()

# Status pokemon
status_pok = Label(janela, text='Status', relief='flat', anchor=CENTER, font=(
    "Fixedsys", 20), bg='white', fg='black')
status_pok.place(x=20, y=300)
# HP
hp_pok = Label(janela, text='', relief='flat', anchor=CENTER,
               font=("Poppins 10"), bg='white', fg='black')
hp_pok.place(x=20, y=340)
# ataque
ataque_pok = Label(janela, text='', relief='flat',
                   anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
ataque_pok.place(x=20, y=360)
# ataque especial
sp_ataque_pok = Label(janela, text='', relief='flat',
                      anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
sp_ataque_pok.place(x=20, y=380)
# defesa
defesa_pok = Label(janela, text='', relief='flat',
                   anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
defesa_pok.place(x=20, y=400)
# defesa especial
sp_defesa_pok = Label(janela, text='', relief='flat',
                      anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
sp_defesa_pok.place(x=20, y=420)
# velocidade
velocidade_pok = Label(janela, text='', relief='flat',
                       anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
velocidade_pok.place(x=20, y=440)
# total
total_pok = Label(janela, text='', relief='flat',
                  anchor=CENTER, font=("Poppins 10 bold"), bg='white', fg='black')
total_pok.place(x=20, y=470)

# Habilidades pokemon
Habilidade_pok = Label(janela, text='Habilidade', relief='flat',
                       anchor=CENTER, font=("Fixedsys", 20), bg='white', fg='black')
Habilidade_pok.place(x=300, y=300)

HB1_pok = Label(janela, text='', relief='flat',
                anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
HB1_pok.place(x=300, y=340)

HB2_pok = Label(janela, text='', relief='flat',
                anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
HB2_pok.place(x=300, y=360)

HB3_pok = Label(janela, text='', relief='flat',
                anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
HB3_pok.place(x=300, y=380)

HB4_pok = Label(janela, text='', relief='flat',
                anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
HB4_pok.place(x=300, y=400)

#Descrição pokemon
descricao_pok = Label(janela, text='Descrição', relief='flat',
                      anchor=CENTER, font=("Fixedsys", 20), bg='white', fg='black')
descricao_pok.place(x=580, y=300)

descricao_pok1 = Label(janela, text='', relief='flat',
                anchor=CENTER, font=("Poppins 10"), bg='white', fg='black')
descricao_pok1.place(x=580, y=400)

# cria Botoes

# Botão 1
image_perfil_1 = Image.open('icone/gengar-94.png')
image_perfil_1 = image_perfil_1.resize((40, 40))
image_perfil_1 = ImageTk.PhotoImage(image_perfil_1)

b_pok_1 = Button(janela, command=lambda: trocar_pokemon('Gengar'), image=image_perfil_1, text='Gengar', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_1.place(x=380, y=10)

# Botão 2
image_perfil_2 = Image.open('icone/aerodactyl-142.png')
image_perfil_2 = image_perfil_2.resize((40, 40))
image_perfil_2 = ImageTk.PhotoImage(image_perfil_2)

b_pok_2 = Button(janela, command=lambda: trocar_pokemon('Aerodactyl'), image=image_perfil_2, text='Aerodactyl', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_2.place(x=380, y=60)

# Botão 3
image_perfil_3 = Image.open('icone/bulbasaur-001.png')
image_perfil_3 = image_perfil_3.resize((40, 40))
image_perfil_3 = ImageTk.PhotoImage(image_perfil_3)

b_pok_3 = Button(janela, command=lambda: trocar_pokemon('Bulbasaur'),  image=image_perfil_3, text='Bulbasaur', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_3.place(x=380, y=110)

# Botão 4
image_perfil_4 = Image.open('icone/charmander-004.png')
image_perfil_4 = image_perfil_4.resize((40, 40))
image_perfil_4 = ImageTk.PhotoImage(image_perfil_4)

b_pok_4 = Button(janela, command=lambda: trocar_pokemon('Charmander'), image=image_perfil_4, text='Charmander', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_4.place(x=380, y=160)

# Botão 5
image_perfil_5 = Image.open('icone/crobat-169.png')
image_perfil_5 = image_perfil_5.resize((40, 40))
image_perfil_5 = ImageTk.PhotoImage(image_perfil_5)

b_pok_5 = Button(janela, command=lambda: trocar_pokemon('Crobat'), image=image_perfil_5, text='Crobat', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_5.place(x=380, y=210)

# Botão 6
image_perfil_6 = Image.open('icone/cubone-104.png')
image_perfil_6 = image_perfil_6.resize((40, 40))
image_perfil_6 = ImageTk.PhotoImage(image_perfil_6)

b_pok_6 = Button(janela, command=lambda: trocar_pokemon('Cubone'), image=image_perfil_6, text='Cubone', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_6.place(x=550, y=10)

# Botão 7
image_perfil_7 = Image.open('icone/mew-151.png')
image_perfil_7 = image_perfil_7.resize((40, 40))
image_perfil_7 = ImageTk.PhotoImage(image_perfil_7)

b_pok_7 = Button(janela, command=lambda: trocar_pokemon('Mew'), image=image_perfil_7, text='Mew', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_7.place(x=550, y=60)

# Botão 1
image_perfil_8 = Image.open('icone/mewtwo-150.png')
image_perfil_8 = image_perfil_8.resize((40, 40))
image_perfil_8 = ImageTk.PhotoImage(image_perfil_8)

b_pok_8 = Button(janela, command=lambda: trocar_pokemon('Mewtwo'), image=image_perfil_8, text='Mewtwo', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_8.place(x=550, y=110)

# Botão 9
image_perfil_9 = Image.open('icone/pikachu-25.png')
image_perfil_9 = image_perfil_9.resize((40, 40))
image_perfil_9 = ImageTk.PhotoImage(image_perfil_9)

b_pok_9 = Button(janela, command=lambda: trocar_pokemon('Pikachu'), image=image_perfil_9, text='Pikachu', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_9.place(x=550, y=160)

# Botão 10
image_perfil_10 = Image.open('icone/squitle-007.png')
image_perfil_10 = image_perfil_10.resize((40, 40))
image_perfil_10 = ImageTk.PhotoImage(image_perfil_10)

b_pok_10 = Button(janela, command=lambda: trocar_pokemon('Squirtle'), image=image_perfil_10, text='Squirtle', width=150,
                  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_10.place(x=550, y=210)

# Botão 11
image_perfil_11 = Image.open('icone/umbreon-197.png')
image_perfil_11 = image_perfil_11.resize((40, 40))
image_perfil_11 = ImageTk.PhotoImage(image_perfil_11)

b_pok_11 = Button(janela, command=lambda: trocar_pokemon('Umbreon'), image=image_perfil_11, text='Umbreon', width=150,
                  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_11.place(x=720, y=10)

# Botão 12
image_perfil_12 = Image.open('icone/vaporeon-134.png')
image_perfil_12 = image_perfil_12.resize((40, 40))
image_perfil_12 = ImageTk.PhotoImage(image_perfil_12)

b_pok_12 = Button(janela, command=lambda: trocar_pokemon('Vaporeon'), image=image_perfil_12, text='Vaporeon', width=150,
                  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_12.place(x=720, y=60)

# Botão 13
image_perfil_13 = Image.open('icone/hypno-097.png')
image_perfil_13 = image_perfil_13.resize((40, 40))
image_perfil_13 = ImageTk.PhotoImage(image_perfil_13)

b_pok_13 = Button(janela, command=lambda: trocar_pokemon('Hypno'), image=image_perfil_13, text='Hypno', width=150,
                  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_13.place(x=720, y=110)

# Botão 14
image_perfil_14 = Image.open('icone/lapras-131.png')
image_perfil_14 = image_perfil_14.resize((40, 40))
image_perfil_14 = ImageTk.PhotoImage(image_perfil_14)

b_pok_14 = Button(janela, command=lambda: trocar_pokemon('Lapras'), image=image_perfil_14, text='Lapras', width=150,
                  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_14.place(x=720, y=160)

# Botão 15
image_perfil_15 = Image.open('icone/scyther-123.png')
image_perfil_15 = image_perfil_15.resize((40, 40))
image_perfil_15 = ImageTk.PhotoImage(image_perfil_15)

b_pok_15 = Button(janela, command=lambda: trocar_pokemon('Scyther'), image=image_perfil_15, text='Scyther', width=150,
                  relief='raised', overrelief=RIDGE, compound=LEFT, ancho=NW, padx=5, font=("Fixedsys", 10), bg='white', fg='black')
b_pok_15.place(x=720, y=210)

janela.mainloop()
