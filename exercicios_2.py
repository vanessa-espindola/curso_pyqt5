import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel

class Janela (QMainWindow):
	def __init__(self):
		super().__init__()

		self.topo = 100
		self.esquerda = 100
		self.largura = 800
		self.altura = 600
		self.titulo = "Primeira Janela"


		botao1 = QPushButton("Botao 1", self)
		botao1.move(250,200)
		botao1.resize(150,80);
		botao1.setStyleSheet("QPushButton {background-color:#0FB600; font:bold; font-size:20 px}")
		botao1.clicked.connect(self.botao1_click)

		botao2 = QPushButton("Botao 2", self)
		botao2.move(450,200)
		botao2.resize(150,80);
		botao2.setStyleSheet("QPushButton {background-color:#FFCCE5; font:bold; font-size:20 px;}")
		botao2.clicked.connect(self.botao2_click)
		self.label_1 = QLabel(self)
		self.label_1.setText("Aperte algum botão")
		self.label_1.move(50,50)
		self.label_1.setStyleSheet("QLabel {font:bold; font-size:30 px;  color: blue}")
		self.label_1.resize(400,25)
		self.CarregarJanela()

	def CarregarJanela(self):
		self.setGeometry (self.topo, self.esquerda, self.largura, self.altura)
		self.setWindowTitle(self.titulo)
		self.show()

	def botao1_click(self):
		self.label_1.setText("O botão 1 foi clicado")
		self.label_1.setStyleSheet("QLabel {font:bold; font-size:30 px;  color: green}")

	def botao2_click(self):
		self.label_1.setText("O botão 2 foi clicado")
		self.label_1.setStyleSheet("QLabel {font:bold; font-size:30 px;  color: red}")

aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())




