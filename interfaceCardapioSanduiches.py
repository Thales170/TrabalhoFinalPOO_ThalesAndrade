"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

# Importa a variável sanduiches do arquivo em python Lersanduicheexcel.py
from Lersanduicheexcel import sanduiches

# Importa a classe abstrata do arquivo Interface
from interface import Interface

#Importa a classe responsável por montar/adicionar/remover itens no carrinho de compras.
from carrinhodecompras import carrinho

# Para a interface gráfica
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

class InterfaceCardapioSanduiches(Interface):
    def __init__(self, sanduiches):
        self.sanduiches = sanduiches
        self.root = None

    def definirFundoTela(self, cor: str, root: tk.Tk) -> None:
        """
        Parâmentro cor: Recebe a cor de fundo.
        Parâmetro root: recebe a guia/janela onde vai configurar o fundo
        """
        root.configure(bg=cor)

    def criarWidgets(self, root: tk.Tk) -> None:
        """
        Parâmetro root: recebe a guia/janela onde vai configurar o fundo
        """
        # Título "Tribo do Thales"
        titulo_fonte = tkfont.Font(family="Lucida Handwriting", size=20, weight="bold", slant="italic")
        titulo1 = tk.Label(root, text="Tribo do Thales", bg="lightgray", fg="navy", font=titulo_fonte) #navy = azul marinho
        titulo1.place(relx=0.05, y=30, anchor='nw')          #Posição do texto.

        # Título "CARDÁPIO DE SANDUÍCHES"
        titulo2_fonte = tkfont.Font(family="Helvetica", size=20, weight="bold")
        titulo2 = tk.Label(root, text="CARDÁPIO DE SANDUÍCHES", bg="lightgray", fg="darkred", font=titulo2_fonte)
        titulo2.place(relx=0.5, y=20, anchor='n')

        # Frame para a lista de sanduíches. FRAME É A MESMA COISA QUE CAIXA.
        frame_sanduiches = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
        
       
        # relwidth: largura relativa do frame (valor entre 0 e 1, onde 1 é 100% da largura do root)
        # relheight: altura relativa do frame (valor entre 0 e 1, onde 1 é 100% da altura do root)
        # relx: posição relativa horizontal do frame (valor entre 0 e 1, onde 0 é o lado esquerdo e 1 é o lado direito do root)
        # rely: posição relativa vertical do frame (valor entre 0 e 1, onde 0 é o topo e 1 é a base do root)
        frame_sanduiches.place(relwidth=0.56, relheight=0.75, relx=0.02, rely=0.15)

        # Exibir os sanduíches
        for i, sanduiche in enumerate(self.sanduiches):
            sanduiche_label = tk.Label(frame_sanduiches, text=f"{i + 1}. {sanduiche.nome} - Preço: R$ {sanduiche.preco}", bg="lightgray", fg="black", font=("Helvetica", 11, "bold"))
            sanduiche_label.pack(anchor='w', padx=10, pady=(5, 0))

            descricao_label = tk.Label(frame_sanduiches, text=sanduiche.descricao, bg="lightgray", fg="black", font=("Times New Roman", 10))
            descricao_label.pack(anchor='w', padx=20, pady=(0, 5))

        # Caixa de diálogo para entrada do NUMERO DO SANDUICHE
        dialog_frame = tk.Frame(root, bg="lightgray")
        
        # relwidth: largura relativa do frame (valor entre 0 e 1, onde 1 é 100% da largura do root)
        # relheight: altura relativa do frame (valor entre 0 e 1, onde 1 é 100% da altura do root)
        # relx: posição relativa horizontal do frame (valor entre 0 e 1, onde 0 é o lado esquerdo e 1 é o lado direito do root)
        # rely: posição relativa vertical do frame (valor entre 0 e 1, onde 0 é o topo e 1 é a base do root)
        dialog_frame.place(relwidth=0.24, relheight=0.2, relx=0.64, rely=0.15)

        # Mensagem para o usuário
        msg_label = tk.Label(dialog_frame, text="Digite o número correspondente ao sanduíche selecionado", bg="lightgray", fg="black")
        msg_label.pack(pady=5)
        
        self.entry_sanduiche_num = tk.Entry(dialog_frame, bg="white", fg="black")
        self.entry_sanduiche_num.pack(pady=5)
        
        # Caixa de diálogo para QUANTIDADE DE SANDUICHES
        dialog_frame2 = tk.Frame(root, bg="lightgray")
        dialog_frame2.place(relwidth=0.2, relheight=0.2, relx=0.66, rely=0.24)

        # Mensagem para o usuário
        msg_label2 = tk.Label(dialog_frame2, text="Quantidade", bg="lightgray", fg="black")
        msg_label2.pack(pady=5)

        self.entry_sanduiche_quantidade = tk.Entry(dialog_frame2, bg="white", fg="black")
        self.entry_sanduiche_quantidade.pack(pady=5)


        # Botão "PRÓXIMO"
        self.btn_proximo = tk.Button(dialog_frame2, text="PRÓXIMO", command=self.proximo)
        self.btn_proximo.pack(pady=5)

        # Botão "VOLTAR"
        btn_voltar = tk.Button(root, text="VOLTAR", command=self.BotaoVoltar)
        btn_voltar.place(relx=0.02, rely=0.95)
        
    def BotaoVoltar(self):
        #VOU FECHAR ESSA INTERFACE 
        self.root.destroy()
        
        # Importa a interface anterior, caso aperte o botão voltar, vai retornar para essa interface. Importei o objeto instanciado.
        from interfaceInicio import interface_inicio
        
        #VOU VOLTAR PARA A INTERFACE DO MENU PRINCIPAL
        interface_inicio.rodarInterface( )

    def proximo(self):
        num_sanduiche = self.entry_sanduiche_num.get()
        quantidade_sanduiche = self.entry_sanduiche_quantidade.get()

        if not self.validarValorDigitado(num_sanduiche):
            messagebox.showerror("Erro", f"Escolha um sanduíche de 1 até {len(self.sanduiches)}.")
        elif not self.validarQuantidadeDigitada(quantidade_sanduiche):
            messagebox.showerror("Erro", "Quantidade de sanduíches não permitida. Favor insira um número de 1 a 50.")
        else:
            num_sanduiche = int(num_sanduiche)
            quantidade_sanduiche = int(quantidade_sanduiche)
            sanduiche = self.sanduiches[num_sanduiche - 1]
            carrinho.addItem({
                'descricao': sanduiche.nome,
                'preco': sanduiche.preco,
                'quantidade': quantidade_sanduiche
            })
            messagebox.showinfo("Seleção", f"Você selecionou o sanduíche {sanduiche.nome}.\nQuantidade: {quantidade_sanduiche}.")
            
            #FECHO ESSA JANELA
            self.root.destroy()
            from interfaceInicio import interface_inicio
            
            #VOU VOLTAR PARA A INTERFACE DO MENU PRINCIPAL
            interface_inicio.rodarInterface( )

    def validarValorDigitado(self, num_sanduiche):
        """
        Parâmetro num_sanduiche: recebe o número do sanduiche digitado pelo usuário
        Retorna True se o numero digitado é adequada, Retorna False se a quantidade não é adequada
        """
        if num_sanduiche.isdigit():
            num_sanduiche = int(num_sanduiche)
            if num_sanduiche >= 1 and num_sanduiche <= len(self.sanduiches):
                return True
            else:
                return False
        else:
            return False
        
    def validarQuantidadeDigitada(self, quantidade_sanduiche):
        """
        Parâmetro quantidade_sanduiche: recebe a quantidade de sanduiche digitada pelo usuário
        Retorna True se a quantidade é adequada, Retorna False se a quantidade não é adequada
        """
        
        if quantidade_sanduiche.isdigit():
            quantidade_sanduiche = int(quantidade_sanduiche)
            return 1 <= quantidade_sanduiche <= 50
        return False

    def rodarInterface(self) -> None:
        # Cria a janela principal
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Cardápio de Sanduíches")
        self.definirFundoTela('lightgray', self.root)
        self.criarWidgets(self.root)
        
        #maxima janela
        self.root.state('zoomed') 
        
        # Roda a interface
        self.root.mainloop()

# Inicializa a interface usando os sanduíches importados do módulo Lersanduicheexcel
interfaceCardapioSanduiches = InterfaceCardapioSanduiches(sanduiches)
