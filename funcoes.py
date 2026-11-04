import tkinter as tk
from tkinter import messagebox

class Carro:
  def __init__(self, nome, placa):
    self.nome = nome
    self.ligado = False
    self.velocidade = 0
    self.placa = placa

  def mudarStatusCarro(self, textoAviso, textoDesc):
    if self.ligado == True:
      self.ligado = False
      textoAviso["text"] = "Carro desligado!"
    else:
      self.ligado = True
      textoAviso["text"] = "Carro ligado!"
    textoDesc["text"] = f"\n === Status do Carro ===\n Nome do carro: {self.nome}\n Velocidade do carro: {self.velocidade}\n Placa carro: {self.placa}"

  def acelerarCarro(self, textoAviso, textoDesc):
    if self.ligado == True:
      self.velocidade += 10
      textoAviso["text"] = "Acelerou com sucesso!"
    else:
      textoAviso["text"] = "Ligue o carro!"
    textoDesc["text"] = f"\n === Status do Carro ===\n Nome do carro: {self.nome}\n Velocidade do carro: {self.velocidade}\n Placa carro: {self.placa}"

  def freiarCarro(self, textoAviso, textoDesc):
    if self.ligado == True:
      if self.velocidade > 0:
        self.velocidade -= 10
        textoAviso["text"] = "Freiou com sucesso!"
      else:
        textoAviso["text"] = "O carro já está na velocidade minima!"
    else:
      textoAviso["text"] = "Ligue o Carro!"
    textoDesc["text"] = f"\n === Status do Carro ===\n Nome do carro: {self.nome}\n Velocidade do carro: {self.velocidade}\n Placa carro: {self.placa}"

  def freioDeMao(self, textoAviso, textoDesc):
    self.velocidade = 0
    textoAviso["text"] = "Você parou o carro!"
    textoDesc["text"] = f"\n === Status do Carro ===\n Nome do carro: {self.nome}\n Velocidade do carro: {self.velocidade}\n Placa carro: {self.placa}"


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def encerrarPrograma(janela):
  messagebox.showwarning("Tchau!", "Nos vemos mais tarde!")
  janela.destroy()



