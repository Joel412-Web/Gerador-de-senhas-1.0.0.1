from tkinter import messagebox
import customtkinter
import string
import random

# Definir Cores a Usar ----------------------------
Co0 = "#808080"
Co1 = "#FFFFFF"

# Função para gerar senha --------------------------
def gerar_senha():
    caracteres = ""
    
    # Verificar quais opções estão selecionadas
    if chkGrandes.get() == 1:
        caracteres += string.ascii_uppercase
    if chkPequenas.get() == 1:
        caracteres += string.ascii_lowercase
    if chkNumeros.get() == 1:
        caracteres += string.digits
    if chkSimbolos.get() == 1:
        caracteres += string.punctuation
    
    comprimento = int(SChars.get())

    # Verificar se o comprimento é maior que zero e se há caracteres disponíveis
    if comprimento < 1 or not caracteres:
        ESenha.delete(0, 'end')
        LStatus.configure(text="Selecione opções válidas e defina o comprimento")
        return

    # Gerar a senha
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    ESenha.delete(0, 'end')
    ESenha.insert(0, senha)
    LStatus.configure(text="Senha gerada com sucesso")

    # Atualizar o label Lchars com o número de caracteres
    Lchars.configure(text=f'Caracteres {comprimento}')

# Função para copiar a senha ----------------------
def copiar_senha():
    Janela.clipboard_clear()
    Janela.clipboard_append(ESenha.get())
    LStatus.configure(text="Senha copiada para a área de transferência")

# Função para limpar a senha ----------------------
def limpar_senha():
    ESenha.delete(0, 'end')
    chkGrandes.deselect()
    chkPequenas.deselect()
    chkNumeros.deselect()
    chkSimbolos.deselect()
    SChars.set(0)
    Lchars.configure(text="Caracteres 0:")
    LStatus.configure(text="Estado ...")

# Função para sair -------------------------------
def sair():
    resposta = messagebox.askyesno("Confirmação", "Deseja sair da aplicação?")
    if resposta:
        Janela.destroy()

# Janela ----------------------------
Janela = customtkinter.CTk()
Janela.geometry('800x220+100+100')
Janela.resizable(0, 0)
Janela.title('Gerador de senhas © Dev Joel Portugal 2024')
Janela.config(bg=Co0)

ESenha = customtkinter.CTkEntry(Janela, width=780, bg_color=Co0, fg_color=Co0, text_color=Co1, border_color="")
ESenha.place(x=10, y=10)

chkGrandes = customtkinter.CTkCheckBox(Janela, text='Letras Grandes', bg_color=Co0, fg_color=Co0, text_color=Co1, border_color="")
chkGrandes.place(x=10, y=45)

chkPequenas = customtkinter.CTkCheckBox(Janela, text='Letras Pequenas', bg_color=Co0, fg_color=Co0, text_color=Co1, border_color="")
chkPequenas.place(x=155, y=45)

chkNumeros = customtkinter.CTkCheckBox(Janela, text='Números', bg_color=Co0, fg_color=Co0, text_color=Co1, border_color="")
chkNumeros.place(x=320, y=45)

chkSimbolos = customtkinter.CTkCheckBox(Janela, text='Símbolos', bg_color=Co0, fg_color=Co0, text_color=Co1, border_color="")
chkSimbolos.place(x=455, y=45)

Lchars = customtkinter.CTkLabel(Janela, text='Caracteres 0', bg_color=Co0, fg_color=Co0, text_color=Co1)
Lchars.place(x=10, y=80)

SChars = customtkinter.CTkSlider(Janela, width=760, bg_color=Co0, fg_color=Co0, from_=1, to=255)  # Adicionado limite mínimo e máximo
SChars.place(x=10, y=115)
SChars.set(0)  # Definindo um valor padrão diferente de 0

BGerar = customtkinter.CTkButton(Janela, text='Gerar', width=65, bg_color=Co0, fg_color=Co0, text_color=Co1, command=gerar_senha)
BGerar.place(x=10, y=150)

Bcopiar = customtkinter.CTkButton(Janela, text='Copiar', width=65, bg_color=Co0, fg_color=Co0, text_color=Co1, command=copiar_senha)
Bcopiar.place(x=85, y=150)

BLimpar = customtkinter.CTkButton(Janela, text='Limpar', width=65, bg_color=Co0, fg_color=Co0, text_color=Co1, command=limpar_senha)
BLimpar.place(x=160, y=150)

BSair = customtkinter.CTkButton(Janela, text='Sair', width=65, bg_color=Co0, fg_color=Co0, text_color=Co1, command=sair)
BSair.place(x=235, y=150)

LStatus = customtkinter.CTkLabel(Janela, text='Estado ...', bg_color=Co0, fg_color=Co0, text_color=Co1)
LStatus.place(x=10, y=185)

Janela.mainloop()
