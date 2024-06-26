import tkinter as interface
import menu
from tkinter import messagebox

janela = None
txtusuario = None
txtsenha = None

def Abrinovajanela():
    usuario = txtusuario.get()
    senha = txtsenha.get()

    if usuario == "admin" and senha == "4321":
        messagebox.showinfo("Sucesso", "Acesso bem-sucedido")
        janela.destroy()
        menu.iniciarJanela()
    else:
        messagebox.showinfo("Erro", "Acesso negado")

def iniciarJanela():
    global txtusuario
    global txtsenha
    global janela
    janela = interface.Tk()
    janela.geometry("400x400")
    janela.title("Exemplo de Tela com Botões")

    frame1 = interface.Frame(janela)
    frame1.pack()

    frameBotao = interface.Frame(janela)
    frameBotao.pack()

    ldlusuario = interface.Label(frame1, text="Usuario")
    ldlusuario.grid(row=0, column=0)

    txtusuario = interface.Entry(frame1)
    txtusuario.grid(row=0, column=1)

    ldlsenha = interface.Label(frame1, text="Senha")
    ldlsenha.grid(row=2, column=0)

    txtsenha = interface.Entry(frame1)
    txtsenha.grid(row=2, column=1)

    btnCadastro = interface.Button(frameBotao, text="Cadastrar", command= Abrinovajanela)
    btnCadastro.pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    iniciarJanela()