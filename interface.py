import matplotlib.pyplot as plt
import tkinter as tk
import PlotarComInterface


def entrada():
    if(str(ed.get()).isnumeric() and int(ed.get()) > 0):
        bt1['text'] = 'Atualizar'
        lb2['text'] = ' '

        plotar.setFases(int(ed.get()))

    else:
        lb2['text'] = 'Valor inválido'


def _quit():
    plotar.test = 'n'
    janela.quit()
    janela.destroy()
    exit()


janela = tk.Tk()
janela.geometry("300x200+200+200")
janela.title("Campo Magnético Girante")
janela["bg"] = "white"

plotar = PlotarComInterface.Plotar(0, janela)

ed = tk.Entry(janela)
ed.place(x=10, y=35)

lb1 = tk.Label(janela, text="Entre com o número de fases: ")
lb1.place(x=10, y=10)
lb1['bg'] = 'white'

lb2 = tk.Label(janela, text=" ")
lb2.place(x=10, y=60)
lb2['bg'] = 'white'

bt1 = tk.Button(janela, width=10, text="Gerar", command=entrada)
bt1.place(x=10, y=85)

bt2 = tk.Button(master=janela, text="Quit", command=_quit)
bt2.pack(side=tk.BOTTOM)


janela.mainloop()
