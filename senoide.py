import numpy as np
import matplotlib.pyplot as plt

class Senoide():
	def __init__(self):
		self.tempo = np.linspace(0, 2*np.pi, 1000)
		plt.ion()

	def setNumero_de_fases(self, numero_de_fases):
		self.numero_de_fases = numero_de_fases

	def plotarOndas(self):
		for i in range(0, self.numero_de_fases):
			plt.plot(self.tempo, np.sin(self.tempo - i*(2*np.pi)/(self.numero_de_fases)))
