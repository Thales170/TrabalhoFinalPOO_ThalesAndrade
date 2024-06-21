"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

# Importa a variável acais do arquivo em python Leracaiexcel.py
from Leracaiexcel import acais

# Importa a classe abstrata do arquivo Interface
from interface import Interface

#Importa a classe responsável por montar/adicionar/remover itens no carrinho de compras.
from carrinhodecompras import carrinho

# Para a interface gráfica
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

class InterfaceCardapioAcais(Interface):
    def __init__(self, acais):
        self.acais = acais
        self.root = None

    def definirFundoTela(self, cor: str, root: tk.Tk) -> None:
        """
        Parâmetro cor: recebe a cor de fundo
        Parâmetro root: recebe a janela/guia que será editada
        """
        root.configure(bg=cor)

    def criarWidgets(self, root: tk.Tk) -> None:
        # Título "Tribo do Thales"
        titulo_fonte = tkfont.Font(family="Lucida Handwriting", size=20, weight="bold", slant="italic")
        titulo1 = tk.Label(root, text="Tribo do Thales", bg="lightgray", fg="navy", font=titulo_fonte)
        titulo1.place(relx=0.05, y=30, anchor='nw')

        # Título "CARDÁPIO DE AÇAÍ"
        titulo2_fonte = tkfont.Font(family="Helvetica", size=20, weight="bold")
        titulo2 = tk.Label(root, text="CARDÁPIO DE AÇAÍ", bg="lightgray", fg="darkred", font=titulo2_fonte)
        titulo2.place(relx=0.5, y=20, anchor='n')

        # Frame para a lista de açaís
        frame_acais = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
        frame_acais.place(relwidth=0.26, relheight=0.65, relx=0.2, rely=0.20)

        # Exibir os açaís
        for i, acai in enumerate(self.acais):
            descricao_fonte = tkfont.Font(family="Helvetica", size=11, weight="bold")
            preco_fonte = tkfont.Font(family="Helvetica", size=11)

            acai_label = tk.Label(frame_acais, text=f"{i + 1}. {acai.descricao}", bg="lightgray", fg="black", font=descricao_fonte)
            acai_label.pack(anchor='w', padx=10, pady=(5, 0))

            preco_label = tk.Label(frame_acais, text=f"Preço: R$ {acai.preco}", bg="lightgray", fg="black", font=preco_fonte)
            preco_label.pack(anchor='w', padx=20, pady=(0, 15))

        # Caixa de diálogo para NUMERO DO AÇAÍ
        dialog_frame = tk.Frame(root, bg="lightgray")
        dialog_frame.place(relwidth=0.24, relheight=0.2, relx=0.54, rely=0.20)

        # Mensagem para o usuário
        msg_label = tk.Label(dialog_frame, text="Digite o número correspondente ao açaí selecionado", bg="lightgray", fg="black")
        msg_label.pack(pady=5)

        self.entry_acai_escolhido = tk.Entry(dialog_frame, bg="white", fg="black", width=20)
        self.entry_acai_escolhido.pack(pady=5)
        
        # Caixa de diálogo para QUANTIDADE DE AÇAÍ
        dialog_frame2 = tk.Frame(root, bg="lightgray")
        dialog_frame2.place(relwidth=0.24, relheight=0.2, relx=0.54, rely=0.30)

        # Mensagem para o usuário
        msg_label2 = tk.Label(dialog_frame2, text="Quantidade", bg="lightgray", fg="black")
        msg_label2.pack(pady=5)

        self.entry_acai_quantidade = tk.Entry(dialog_frame2, bg="white", fg="black")
        self.entry_acai_quantidade.pack(pady=5)

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
        num_acai = self.entry_acai_escolhido.get()
        quantidade_acai = self.entry_acai_quantidade.get()

        if not self.validarValorDigitado(num_acai):
            messagebox.showerror("Erro", f"Escolha um açaí de 1 até {len(self.acais)}.")
        elif not self.validarQuantidadeDigitada(quantidade_acai):
            messagebox.showerror("Erro", "Quantidade de açaís não permitida. Favor insira um número de 1 a 50.")
        else:
            num_acai = int(num_acai)
            quantidade_acai = int(quantidade_acai)
            acai = self.acais[num_acai-1]
            
            carrinho.addItem({
                'descricao': acai.descricao,
                'preco': acai.preco,
                'quantidade': quantidade_acai
            })
            
            messagebox.showinfo("Seleção", f"Você selecionou o açaí {self.acais[num_acai - 1].descricao}.\nQuantidade: {quantidade_acai}.")
            
            #FECHO ESSA JANELA
            self.root.destroy()
            from interfaceInicio import interface_inicio
            
            #VOU VOLTAR PARA A INTERFACE DO MENU PRINCIPAL
            interface_inicio.rodarInterface( )
            

    def validarValorDigitado(self, num_acai):
        """
        Parâmetro num_acai: recebe o número do açaí digitado pelo usuário
        Retorna: True se o numero digitado é adequada, Retorna False se o número do açaí não é adequado
        """
        if num_acai.isdigit():
            num_acai = int(num_acai)
            if num_acai >= 1 and num_acai <= len(self.acais):
                return True
            else:
                return False
        else:
            return False
        
    def validarQuantidadeDigitada(self, quantidade_acai):
        """
        Parâmetro quantidade_acai: recebe o número do açaí digitado pelo usuário
        Retorna: True se a quatidade é adequada, Retorna False se a quantidade do açaí não é adequado
        """
        if quantidade_acai.isdigit():
            quantidade_acai = int(quantidade_acai)
            return 1 <= quantidade_acai <= 50
        return False
    

    def rodarInterface(self) -> None:
        # Cria a janela principal
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Cardápio de Açaí")
        self.definirFundoTela('lightgray', self.root)
        self.criarWidgets(self.root)
        
        #maxima janela
        self.root.state('zoomed') 
        
        # Roda a interface
        self.root.mainloop()

# Inicializa a interface usando os açaís importados do módulo Leracaiexcel
interfaceCardapioAcai = InterfaceCardapioAcais(acais)
