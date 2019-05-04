import matplotlib.pyplot as plt
from threading import Thread
from time import time
import Estator
import campoMagnetico
import tkinter as tk
import senoide

class Plotar():
    def __init__(self, numero_de_fases, janela):
        self.janela = janela
        self.test = 'n'
        self.indicador = True
        Thread(target=self.iniciaBotao).start()

    def criaEstator(self):
        self.estator.criaBlocoEstator()
        self.estator.criaBobinas()

    def calculaCampo(self):
        try:
            self.campoMagnetico.calculaCampoMagnetico(time()-self.tempoInicial)
        except KeyboardInterrupt:
            exit()

    def plotaCampo(self):
        self.campoMagnetico.plotaCampo()

    def stopProg(self):
        self.test = 'n'
        self.indicador = True

    def startProg(self):
        self.test = 'y'

        if self.indicador:
            lb = tk.Label(self.janela, text="Antes de tudo, aperte Stop")
            lb.place(x=120, y=125)
            lb['bg'] = 'white'

            self.indicador = False
            self.play()

    def setFases(self, numero_de_fases):
        self.numero_de_fases = numero_de_fases

    def iniciaBotao(self):
        bt = tk.Button(self.janela, width=10, text="Start", command=self.startProg)
        bt.place(x=10, y=120)

        bt1 = tk.Button(self.janela, width=10, text="Stop", command=self.stopProg)
        bt1.place(x=10, y=155)

    def play(self):
        plt.ion()
        plt.grid(True)
        plt.axis('equal')
        plt.xlim(-(self.numero_de_fases/2 + 1), self.numero_de_fases/2 + 1)
        plt.ylim(-(self.numero_de_fases/2 + 1), self.numero_de_fases/2 + 1)

        self.estator        = Estator.Estator(self.numero_de_fases)
        self.campoMagnetico = campoMagnetico.campoMagnetico(self.numero_de_fases)
        self.sin            = senoide.Senoide()

        self.sin.setNumero_de_fases(self.numero_de_fases)


        self.tempoInicial = time()

        
        while(self.test == 'y'):
            self.calculaCampo()
            plt.pause(0.000000001)

            plt.figure(1)
            plt.title('Correntes')
            plt.clf()
            self.sin.plotarOndas()

            plt.figure(2)
            plt.title('Campo Magnético Girante')
            plt.clf()
            self.criaEstator()
            self.plotaCampo()
