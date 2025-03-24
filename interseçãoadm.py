from tkinter import *
from tkinter import ttk
import subprocess  # Importar o módulo subprocess

# Criar nova janela para os botões
jan_botao = Tk()
jan_botao.title("Menu Principal ADM")
jan_botao.geometry("600x300")
jan_botao.configure(background="purple")
jan_botao.resizable(width=False, height=False)

Titulo = Label(jan_botao, text="Menu Principal:", font=("Century Gothic", 25), bg="red", fg="White")
Titulo.place(x=1, y=50)

# Funções para os novos botões
def funcionario():
    subprocess.Popen(["python", "Tela_funcionario_adm.py"])  # Executar Tela_funcionario.py como um novo processo

def produto():
    subprocess.Popen(["python", "Tela_produto_adm.py"])

def fornecedor():
    subprocess.Popen(["python", "Tela_fornecedor_adm.py"])

# Adicionar novos botões à nova janela
FuncionarioButton = ttk.Button(jan_botao, text="Funcionário", width=15, command=funcionario)
FuncionarioButton.place(x=150, y=180)

ProdutoButton = ttk.Button(jan_botao, text="Produto", width=15, command=produto)
ProdutoButton.place(x=300, y=180)

FornecedorButton = ttk.Button(jan_botao, text="Fornecedor", width=15, command=fornecedor)
FornecedorButton.place(x=450, y=180)

jan_botao.mainloop()