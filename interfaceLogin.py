"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

# Importa a classe abstrata do arquivo Interface
from interface import Interface

# Importa a classe que contém a interface do MENU inicial
from interfaceInicio import InterfaceInicio

# Para a interface gráfica
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class InterfaceLogin(Interface):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro")
        self.definirFundoTela('lightgray')
        self.criarWidgets()

    def definirFundoTela(self, cor: str) -> None:
        """
        Parâmentro cor: Recebe a cor que será usada como background da guia
        """
        self.root.configure(bg=cor)

    def criarWidgets(self) -> None:
        # Cria a fonte personalizada para o título
        self.titulo_fonte = tkfont.Font(family="Lucida Handwriting", size=35, weight="bold")
        
        # Cria o título e posiciona centralizado no topo
        self.titulo = tk.Label(self.root, text="Tribo do Thales", bg="lightgray", fg="navy", font=self.titulo_fonte,)
        self.titulo.place(relx=0.5, y=50, anchor='n')
        
        # Título "LOGIN"
        self.titulo2_fonte = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.titulo2 = tk.Label(self.root, text="LOGIN", bg="lightgray", fg="darkred", font=self.titulo2_fonte)
        self.titulo2.place(relx=0.5, y=190, anchor='n')
        
        # Cria um frame/conteiner/caixinha de diálogo centralizado com fundo cinza claro
        self.frame = tk.Frame(self.root, bg="lightgray", bd=2, relief="solid")
        self.frame.place(relx=0.5, rely=0.49,relwidth=0.22, relheight=0.40, anchor='center')

        # Cria os widgets/rótulos dentro do contêiner. São as mensagens dentro do contêiner
        self.label_cpf = tk.Label(self.frame, text="CPF (apenas números)", bg="lightgray", fg="black",font=("Arial", 14))
        self.entry_cpf = tk.Entry(self.frame, bg="white", fg="black")

        self.label_nome_completo = tk.Label(self.frame, text="Nome Completo", bg="lightgray", fg="black",font=("Arial", 14))
        self.entry_nome_completo = tk.Entry(self.frame, bg="white", fg="black")
        
        self.label_whatsaap = tk.Label(self.frame, text="WhatsApp\n(Ex:31999075892)",bg="lightgray",fg ="black", font=("Arial", 14))
        self.entry_whatsaap = tk.Entry(self.frame, bg="white",fg="black")

        # Quando o botão "Salvar" é clicado, a função salvar é chamada
        self.button_salvar = tk.Button(self.frame, text="Salvar", command=self.salvar, bg="white", fg="black")

        # Posiciona os widgets no frame
        self.label_cpf.pack(pady=8)
        self.entry_cpf.pack(pady=8)

        self.label_nome_completo.pack(pady=8)
        self.entry_nome_completo.pack(pady=8)
        
        self.label_whatsaap.pack(pady=8)
        self.entry_whatsaap.pack(pady=8)

        self.button_salvar.pack(pady=10)

    def validarCPF(self, cpf: str) -> bool:
        """
        Parâmentro cpf: Recebe o cpf digitado pelo usuário
        Retorna: True se a cpf for adequado, Retorna False se o cpf não for adequado
        """
        return cpf.isdigit() and len(cpf) == 11

    def validarNomeCompleto(self, nome_completo: str) -> bool:
        """
        Parâmentro nome_complet: Recebe o nome digitado pelo usuário
        Retorna: True se o nome for adequado (pelo menos 2 palavras e não tem algarismo numérico), Retorna False se o nome não for adequado
        """
        palavras = nome_completo.split()
        # Verifica se todas as palavras são alfabéticas e se há pelo menos duas palavras
        todas_palavras_sao_alfabeticas = all(palavra.isalpha() for palavra in palavras)
        tem_ao_menos_duas_palavras = len(palavras) >= 2
        return todas_palavras_sao_alfabeticas and tem_ao_menos_duas_palavras
    
    def validarWhatsaap(self,whatsaap:str) -> bool:
        """
        Parâmentro whatsapp: Recebe o whatsapp digitado pelo usuário
        Retorna: True se o whatsapp for adequado, Retorna False se o whatsaap não for adequado
        """
        return whatsaap.isdigit() and len(whatsaap) == 11

    def salvar(self) -> None:
        cpf = self.entry_cpf.get()
        nome_completo = self.entry_nome_completo.get()
        whatsapp = self.entry_whatsaap.get()

        if not self.validarCPF(cpf):
            messagebox.showerror("Erro", "CPF inválido. Certifique-se de que contém 11 dígitos e apenas números.")
            return

        if not self.validarNomeCompleto(nome_completo):
            messagebox.showerror("Erro", "Nome Completo inválido. Certifique-se de que contém apenas letras e ao menos duas palavras.")
            return
        
        if not self.validarWhatsaap(whatsapp):
            messagebox.showerror("Erro","WhatsApp inválido. Certifique-se de que contém 11 dígitos e apenas números.")
            return

        #VOU FECHAR ESSA INTERFACE 
        messagebox.showinfo("Informação", "Dados salvos com sucesso!")
        self.root.destroy()
        
        #VOU ABRIR A INTERFACE DO MENU INICIAL
        interface_inicio = InterfaceInicio( )
        interface_inicio.rodarInterface( )

    def rodarInterface(self) -> None:
        #maxima janela
        self.root.state('zoomed') 
        self.root.mainloop()

# Instancia o objeto interface_login
interface_login = InterfaceLogin()

"""
BASICAMENTE ESSE CÓDIGO SERVE PARA EXIBIR A INTERFACE DE LOGIN.
ALÉM DISSO, EU VOU PEGAR ESSA CLASSE 'InterfaceLogin' E VOU IMPORTAR ELA PARA OUTROS ARQUIVOS.
VOU IMPORTAR ESSA CLASSE E ACESSAR AS VARIÁVEIS CPF, NOME COMPLETO E WHATSAPP.
"""