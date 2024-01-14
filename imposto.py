from tkinter import *
from tkinter import messagebox
import math
import tkinter as tk
import webbrowser

def instrucoes():
    messagebox.showinfo(tela, message='* Esta ferramenta foi feita para calcular um valor bruto atravéz de um valor líquido \n\n* Para isso você deve digitar no primeiro campo o valor líquido que deseja obter \n\n * Em seguida selecione quais impostos serão aplicados neste valor. Os impostos são ISS e INSS \n\n* Depois é só clicar no botão "calcular" e será exibido no campo abaixo o valor bruto aproximado para chegar no valor liquido que foi digitado')

def sobre():

    def ver_mais():
        url = 'https://www.instagram.com/gabrielnascimento_k/'
        webbrowser.open(url)

    tela_sobre = Toplevel(tela)
    tela_sobre.geometry('350x100+500+350')
    tx = Label(tela_sobre, text='Esta ferramenta foi desenvolvida por Gabriel Kemerson\n\n')
    tx.pack()
    bt_sobre = Button(tela_sobre, text='Ver mais', command=ver_mais)
    bt_sobre.pack()

def calcular():

    try:
        valor_inicial_liquido = float(
            valor.get().replace('.', '').replace(',', '.').replace(' ', '')
        )
        valor_imposto = 0.0

        if issvar.get() == True:
            valor_imposto += 0.05

        if inssvar.get() == True:
            valor_imposto += 0.11

        taxa_para_teste = valor_imposto
        valor_imposto = 1 - valor_imposto

        if valor_imposto == 1.0:
            messagebox.showwarning(tela, message='Você deve selecionar pelomenos um imposto')

        else:
            valor_bruto = math.floor((valor_inicial_liquido / valor_imposto) * 100) / 100
            val_teste = valor_bruto - math.floor((valor_bruto * taxa_para_teste) * 100) / 100
            
            if val_teste != valor_inicial_liquido:
                messagebox.showwarning(title='',
                message='O valor Calculado não é exato!'
            )
            
            bruto_formatado = str(valor_bruto)

            bruto_formatado = bruto_formatado.replace('.', ',')
            bruto_ent.delete(0, END)
            bruto_ent.insert(0, bruto_formatado)

    except:
        messagebox.showerror(tela, message='Digite um valor válido!')


tela = Tk()
tela.title('Calculo de impostos')
tela.geometry('400x200+450+200')
tela.resizable(False, False)
barra_menu = tk.Menu(tela)
tela.config(menu=barra_menu)

aba_cinfig = tk.Menu(barra_menu, tearoff=0)
aba_cinfig.add_command(label='Instruções', command=instrucoes)
aba_cinfig.add_command(label='sobre', command=sobre)
barra_menu.add_cascade(label='Configurações', menu=aba_cinfig)

issvar = BooleanVar()
inssvar = BooleanVar()

lb = Label(tela, text='Digite um valor liquido:')
lb.place(x = 30, y = 10)

valor = Entry(tela, width=20)
valor.place(x = 33, y = 35)

iss = Checkbutton(tela,text='ISS       5%', variable=issvar)
iss.place(x=250, y=25)

inss = Checkbutton(tela,text='INSS    11%', variable=inssvar)
inss.place(x=250, y=50)

bt = Button(tela,text='calcular', command=calcular)
bt.place(x = 250, y = 120)

lb2 = Label(tela, text='Valor bruto aproximado:')
lb2.place(x = 30, y = 95)

bruto_ent = Entry(tela, width=20)
bruto_ent.place(x = 33, y = 120)

tela.mainloop()
