# Admitindo que a amplitude máxima de FMM é 1
import matplotlib.pyplot as plt
import numpy as np

class campoMagnetico():
    def __init__(self, numero_de_fases):
        self.numero_de_fases = numero_de_fases

    def calculaCampoMagnetico(self, tempo):
        self.x = 0
        self.y = 0

        for i in range(0, self.numero_de_fases, 1):
            self.x = self.x + np.cos(i*(2*np.pi)/(self.numero_de_fases) + np.pi/2) * np.cos(tempo - i*(2*np.pi)/(self.numero_de_fases))
            self.y = self.y + np.sin(i*(2*np.pi)/(self.numero_de_fases) + np.pi/2) * np.cos(tempo - i*(2*np.pi)/(self.numero_de_fases))

    def plotaCampo(self):
        plt.plot([0, self.x], [0, self.y], c='#ff0000')
