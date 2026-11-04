import tkinter as tk
from tkinter import messagebox
import funcoes


carros = [
    funcoes.Carro("Saveiro do Leandro", "POG6769"),
    funcoes.Carro("Helicoptero do Oliver", "DCLDQF"),
    funcoes.Carro("Peugeot do Jonathan", "M15ÉRI4")
    ]

janela = tk.Tk()

janela.title("Jogo dos carros")
janela.geometry("500x500")

textoPag = tk.Label(janela, text="Seja bem vindo ao meu programa, \n Qual carro você deseja dirigir?", font=("Arial", 16))
textoPag.pack(pady=50)

frameBtnCar = tk.Frame(janela)
frameBtnCar.pack(pady=50)

botaoLea = tk.Button(frameBtnCar, text=carros[0].nome, width=15, height=3, command=lambda: aoClique(carros[0]))
botaoOli = tk.Button(frameBtnCar, text=carros[1].nome, width=15, height=3, command=lambda: aoClique(carros[1]))
botaoJon = tk.Button(frameBtnCar, text=carros[2].nome, width=15, height=3, command=lambda: aoClique(carros[2]))
botaoSair = tk.Button(frameBtnCar, text="Sair do programa", width=15, height=3, command=lambda: funcoes.encerrarPrograma(janela))
botaoLea.pack()
botaoOli.pack()
botaoJon.pack()
botaoSair.pack()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   
def aoClique(carro):
    textoPag["text"] = f"O carro escolhido foi {carro.nome} \n Oque voce deseja fazer?"
    textoPag.pack()

    for widget in janela.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
            
    descCar = tk.Label(janela, text=f"\n === Status do Carro ===\n Nome do carro: {carro.nome}\n Velocidade do carro: {carro.velocidade}\n Placa carro: {carro.placa}", font=("Arial", 16))
    descCar.pack(pady=20)

    frameMetCar = tk.Frame(janela)
    frameMetCar.pack(pady=30)

    botaoLig = tk.Button(frameMetCar, text="Ligar Carro", width=15, height=3, command=lambda: carro.mudarStatusCarro(textoPag, descCar))
    botaoAce = tk.Button(frameMetCar, text="Acelerar Carro", width=15, height=3, command=lambda: carro.acelerarCarro(textoPag, descCar))
    botaoFre = tk.Button(frameMetCar, text="Freiar Carro", width=15, height=3, command=lambda: carro.freiarCarro(textoPag, descCar))
    botaoFreM = tk.Button(frameMetCar, text="Puxar Freio de Mão", width=15, height=3, command=lambda: carro.freioDeMao(textoPag, descCar))
    botaoSair = tk.Button(frameMetCar, text="Sair do programa", width=15, height=3, command=lambda: funcoes.encerrarPrograma(janela))
    botaoLig.pack()
    botaoAce.pack()
    botaoFre.pack()
    botaoFreM.pack()
    botaoSair.pack()

    
janela.mainloop()