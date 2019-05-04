import matplotlib.pyplot as plt
import numpy as np

class Estator():
    def __init__(self, numero_de_fases):
        self.numero_de_fases = numero_de_fases
        self.x = np.linspace(0, 2*np.pi, 100)

        if(self.numero_de_fases == 1):
            self.tamanho_do_bloco = 1.2

        elif(self.numero_de_fases == 2):
            self.tamanho_do_bloco = 1.7

        else:
            self.tamanho_do_bloco = self.numero_de_fases/2

    def criaBlocoEstator(self):
        plt.grid(True)
        plt.axis('equal')
        plt.xlim(-(self.tamanho_do_bloco + 1), self.tamanho_do_bloco + 1)
        plt.ylim(-(self.tamanho_do_bloco + 1), self.tamanho_do_bloco + 1)
        
        plt.plot(self.tamanho_do_bloco*np.cos(self.x), self.tamanho_do_bloco*np.sin(self.x), c='#000000')
        plt.plot((self.tamanho_do_bloco+0.2)*np.cos(self.x), (self.tamanho_do_bloco+0.2)*np.sin(self.x), c='#000000')
        
    def criaBobinas(self):
        plt.grid(True)
        plt.axis('equal')
        plt.xlim(-(self.numero_de_fases/2 + 1), self.numero_de_fases/2 + 1)
        plt.ylim(-(self.numero_de_fases/2 + 1), self.numero_de_fases/2 + 1)

        for i in range(0, 2*self.numero_de_fases, 1):
            plt.plot((self.tamanho_do_bloco+0.1)*np.cos(i*(2*np.pi)/(2*self.numero_de_fases))+0.1*np.cos(self.x), 
                     (self.tamanho_do_bloco+0.1)*np.sin(i*(2*np.pi)/(2*self.numero_de_fases))+0.1*np.sin(self.x), c='#000000')
            
    def play(self):
        plt.grid(True)
        plt.show()