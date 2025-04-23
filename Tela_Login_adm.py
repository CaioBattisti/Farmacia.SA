from tkinter import *
from tkinter import ttk
from DataBase_adm import Database  # Certifique-se de que este módulo está correto
from tkinter import messagebox
import subprocess

# Função para abrir a janela com os botões "Funcionário", "Produto" e "Fornecedor"
def abrir_intersecao():
    subprocess.Popen(["python", "interseçãoadm.py"])  # Executa o código da janela com os botões

# Tela de login
jan = Tk()
jan.title("Login de ADM:")
jan.geometry("600x300")
jan.configure(background="purple")
jan.resizable(width=False, height=False)

Titulo = Label(jan, text="Login:", font=("Century Gothic", 25), bg="red", fg="White")
Titulo.place(x=1, y=50)

# Adicionar campos de usuário e senha
NomeLabel = Label(jan, text="Nome: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
NomeLabel.place(x=1, y=125)
NomeEntry = ttk.Entry(jan, width=30)
NomeEntry.place(x=60, y=125)

senhaLabel = Label(jan, text="Senha: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
senhaLabel.place(x=1, y=155)
senhaEntry = ttk.Entry(jan, width=30, show="*")  # Oculte a senha com "*"
senhaEntry.place(x=55, y=155)

# Função de login
def Login():
    usuario = NomeEntry.get()
    senha = senhaEntry.get()

    # Conectar ao banco de dados
    try:
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        # Consulta para verificar as credenciais
        cursor.execute("SELECT * FROM adm WHERE nome = %s AND senha = %s", (usuario, senha))
        VerifiyLogin = cursor.fetchone()

        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", message="Acesso Confirmado. Bem-vindo!")
            abrir_intersecao()  # Chama a função para abrir a nova janela
        else:
            messagebox.showinfo(title="Info Login", message="Acesso Negado. Verifique se o cadastro está no sistema.")

    except Exception as e:
        messagebox.showerror(title="Erro de Conexão", message=f"Ocorreu um erro: {e}")

    finally:
        # Fecha a conexão com o banco
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Função para registrar novo usuário
def registrar():
    # Remover botões de Login
    LoginButton.place_forget()
    RegisterButton.place_forget()

    # Inserir widgets de cadastro
    CPFLabel = Label(jan, text="CPF:", font=("Century Gothic", 10), bg="orange", fg="White")
    CPFLabel.place(x=250, y=125)
    CPFEntry = ttk.Entry(jan, width=30)
    CPFEntry.place(x=305, y=125)

    EmailLabel = Label(jan, text="Email:", font=("Century Gothic", 10), bg="orange", fg="White")
    EmailLabel.place(x=250, y=155)
    EmailEntry = ttk.Entry(jan, width=30)
    EmailEntry.place(x=305, y=155)

    # Função para registrar no banco de dados
    def RegistrarNoBanco():
        nome = NomeEntry.get()
        email = EmailEntry.get()
        CPF = CPFEntry.get()
        senha = senhaEntry.get()

        if nome == "" or email == "" or CPF == "" or senha == "":
            messagebox.showerror(title="Erro de Registro", message="Preencha todos os campos!")
        else:
            try:
                db = Database()
                conn = db.get_connection()
                cursor = conn.cursor()

                # Verificar se o usuário já existe
                cursor.execute("SELECT * FROM adm WHERE nome = %s", (nome,))
                VerifiyLogin = cursor.fetchone()
                if VerifiyLogin:
                    messagebox.showerror(title="Erro de Registro", message="ADM já cadastrado!")
                else:
                    # Inserir novo usuário
                    cursor.execute("INSERT INTO adm (nome, email, CPF, senha) VALUES (%s, %s, %s, %s)",
                                   (nome, email, CPF, senha))
                    conn.commit()
                    messagebox.showinfo(title="Registro", message="ADM registrado com sucesso!")

                    # Limpar campos após o registro
                    NomeEntry.delete(0, END)
                    EmailEntry.delete(0, END)
                    CPFEntry.delete(0, END)
                    senhaEntry.delete(0, END)

            except Exception as e:
                messagebox.showerror(title="Erro de Conexão", message=f"Ocorreu um erro: {e}")

            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

    Register = ttk.Button(jan, text="Registrar", width=15, command=RegistrarNoBanco)
    Register.place(x=150, y=225)

    # Função para voltar à tela de login
    def VoltarLogin():
        CPFLabel.place_forget()
        CPFEntry.place_forget()
        EmailLabel.place_forget()
        EmailEntry.place_forget()
        Register.place_forget()
        Voltar.place_forget()

        # Trazer de volta os widgets de login
        LoginButton.place(x=150, y=180)
        RegisterButton.place(x=300, y=180)

    Voltar = ttk.Button(jan, text="Voltar", width=15, command=VoltarLogin)
    Voltar.place(x=300, y=225)

# Botões principais
LoginButton = ttk.Button(jan, text="Login", width=15, command=Login)
LoginButton.place(x=150, y=180)

RegisterButton = ttk.Button(jan, text="Registrar", width=15, command=registrar)
RegisterButton.place(x=300, y=180)

jan.mainloop()
