
# importando tkinter
from tkinter import *
from tkinter import ttk

# cores

cor1 = "#3b3b3b"  # preta
cor2 = "#feffff"  # branca
cor3 = "#38576b"  # azul carregado
cor4 = "#ECEFF1"  # cinzenta
cor5 = "#FFAB40"  # laranja



janela = Tk()
janela.title("Calculadora")
janela.geometry("260x350")
janela.config(bg=cor1)



#criando frames
frame_tela = Frame(janela, width=260, height=[50], bg=cor3)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=260, height=[350])
frame_corpo.grid(row=1, column=0)


# Variavel todos os valores

todos_valores = ""


# Criando label
valor_texto = StringVar()

# Criando funcoes

def entrada_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)



    # passando o valor para a a tela
    valor_texto.set(todos_valores)

# funcao para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


# funcao de limpar a tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")





app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 17'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# criando botoes da Primeira fileira

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=9, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrada_valores("%"), text="%", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=115, y=0)
b_3 = Button(frame_corpo, command = lambda: entrada_valores("/"),text="/", width=7, height=2, bg=cor5, fg=cor2, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=171, y=0)

# criando botoes da Segunda fileira

b_4 = Button(frame_corpo, command = lambda: entrada_valores("7"),text="7", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=60)
b_5 = Button(frame_corpo, command = lambda: entrada_valores("8"),text="8", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=57, y=60)
b_6 = Button(frame_corpo, command = lambda: entrada_valores("9"),text="9", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=114, y=60)
b_7 = Button(frame_corpo, command = lambda: entrada_valores("*"),text="*", width=7, height=2, bg=cor5, fg=cor2, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=171, y=60)

# criando botoes da Terceira fileira

b_8 = Button(frame_corpo, command = lambda: entrada_valores("4"),text="4", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=120)
b_9 = Button(frame_corpo, command = lambda: entrada_valores("5"),text="5", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=57, y=120)
b_10 = Button(frame_corpo, command = lambda: entrada_valores("6"),text="6", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=114, y=120)
b_11 = Button(frame_corpo, command = lambda: entrada_valores("-"),text="-", width=7, height=2, bg=cor5, fg=cor2, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=171, y=120)

# criando botoes da Quarta fileira

b_12 = Button(frame_corpo, command = lambda: entrada_valores("1"),text="1", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=180)
b_13 = Button(frame_corpo, command = lambda: entrada_valores("2"),text="2", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=57, y=180)
b_14 = Button(frame_corpo, command = lambda: entrada_valores("3"),text="3", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=114, y=180)
b_15 = Button(frame_corpo, command = lambda: entrada_valores("+"),text="+", width=7, height=2, bg=cor5, fg=cor2, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=171, y=180)

# criando botoes da Quinta fileira

b_16 = Button(frame_corpo, command = lambda: entrada_valores("0"),text="0", width=9, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=240)
b_17 = Button(frame_corpo, command = lambda: entrada_valores("."),text=".", width=4, height=2, bg=cor4, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=115, y=240)
b_17 = Button(frame_corpo, command = calcular,text="=", width=7, height=2, bg=cor5, fg=cor2, font=('Ivy 13  bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=171, y=240)


janela.resizable(False, False)
janela.mainloop()