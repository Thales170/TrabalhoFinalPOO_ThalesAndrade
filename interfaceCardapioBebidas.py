"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

# Importa a variável bebidas do arquivo em python Lerbebidaexcel.py
from Lerbebidaexcel import bebidas

# Importa a classe abstrata do arquivo Interface
from interface import Interface

#Importa a classe responsável por montar/adicionar/remover itens no carrinho de compras.
from carrinhodecompras import carrinho

# Para a interface gráfica
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

class InterfaceCardapioBebidas(Interface):
    def __init__(self, bebidas):
        self.bebidas = bebidas
        self.root = None
        

    def definirFundoTela(self, cor: str, root: tk.Tk) -> None:
        """
        Parâmetro cor: recebe a cor de fundo
        Parâmetro root: recebe a janela/guia que será editada
        """
        root.configure(bg=cor)

    def criarWidgets(self, root: tk.Tk) -> None:
        """
        Parâmetro root: recebe a janela/guia que será editada
        """
        # Título "Tribo do Thales"
        titulo_fonte = tkfont.Font(family="Lucida Handwriting", size=20, weight="bold", slant="italic")
        titulo1 = tk.Label(root, text="Tribo do Thales", bg="lightgray", fg="navy", font=titulo_fonte)
        titulo1.place(relx=0.05, y=30, anchor='nw')

        # Título "CARDÁPIO DE BEBIDAS"
        titulo2_fonte = tkfont.Font(family="Helvetica", size=20, weight="bold")
        titulo2 = tk.Label(root, text="CARDÁPIO DE BEBIDAS", bg="lightgray", fg="darkred", font=titulo2_fonte)
        titulo2.place(relx=0.5, y=20, anchor='n')

        # Frame para a lista de bebidas
        frame_bebidas = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
        frame_bebidas.place(relwidth=0.26, relheight=0.82, relx=0.2, rely=0.13)

        # Exibir as bebidas
        for i, bebida in enumerate(self.bebidas):
            descricao_fonte = tkfont.Font(family="Helvetica", size=11, weight="bold")
            preco_fonte = tkfont.Font(family="Helvetica", size=11)

            bebida_label = tk.Label(frame_bebidas, text=f"{i + 1}. {bebida.descricao}", bg="lightgray", fg="black", font=descricao_fonte)
            bebida_label.pack(anchor='w', padx=10, pady=(3, 0))

            preco_label = tk.Label(frame_bebidas, text=f"Preço: R$ {bebida.preco}", bg="lightgray", fg="black", font=preco_fonte)
            preco_label.pack(anchor='w', padx=20, pady=(0, 8))

        # Caixa de diálogo para entrada do NUMERO DA BEBIDA
        dialog_frame = tk.Frame(root, bg="lightgray")
        dialog_frame.place(relwidth=0.24, relheight=0.2, relx=0.54, rely=0.20)

        # Mensagem para o usuário
        msg_label = tk.Label(dialog_frame, text="Digite o número correspondente à bebida selecionada", bg="lightgray", fg="black")
        msg_label.pack(pady=5)

        self.entry_bebida_escolhida = tk.Entry(dialog_frame, bg="white", fg="black", width=20)
        self.entry_bebida_escolhida.pack(pady=5)
        
        # Caixa de diálogo para QUANTIDADE DA BEBIDA
        dialog_frame2 = tk.Frame(root, bg="lightgray")
        dialog_frame2.place(relwidth=0.24, relheight=0.2, relx=0.54, rely=0.30)

        # Mensagem para o usuário
        msg_label2 = tk.Label(dialog_frame2, text="Quantidade", bg="lightgray", fg="black")
        msg_label2.pack(pady=5)

        self.entry_bebida_quantidade = tk.Entry(dialog_frame2, bg="white", fg="black")
        self.entry_bebida_quantidade.pack(pady=5)

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
        num_bebida = self.entry_bebida_escolhida.get()
        quantidade_bebida = self.entry_bebida_quantidade.get()

        if not self.validarValorDigitado(num_bebida):
            messagebox.showerror("Erro", f"Escolha uma bebida de 1 até {len(self.bebidas)}.")
        elif not self.validarQuantidadeDigitada(quantidade_bebida):
            messagebox.showerror("Erro", "Quantidade de bebidas não permitida. Favor insira um número de 1 a 50.")
        else:
            num_bebida = int(num_bebida)
            quantidade_bebida = int(quantidade_bebida)
            bebida = self.bebidas[num_bebida-1]
            
            carrinho.addItem({
                'descricao': bebida.descricao,
                'preco': bebida.preco,
                'quantidade': quantidade_bebida
            })
            
            messagebox.showinfo("Seleção", f"Você selecionou a bebida {self.bebidas[num_bebida - 1].descricao}.\nQuantidade: {quantidade_bebida}.")
            
            #FECHO ESSA JANELA
            self.root.destroy()
            from interfaceInicio import interface_inicio
            
            #VOU VOLTAR PARA A INTERFACE DO MENU PRINCIPAL
            interface_inicio.rodarInterface( )
            

    def validarValorDigitado(self, num_bebida):
        """
        Parâmetro num_bebida: recebe o número da bebida digitado pelo usuário
        Retorna True se o numero digitado é adequada, Retorna False se a quantidade não é adequada
        """
        if num_bebida.isdigit():
            num_bebida = int(num_bebida)
            if num_bebida >= 1 and num_bebida <= len(self.bebidas):
                return True
            else:
                return False
        else:
            return False
        
    def validarQuantidadeDigitada(self, quantidade_bebida):
        """
        Parâmetro quantidade_pizza: recebe a quantidade de bebida digitado pelo usuário
        Retorna True se o numero digitado é adequada, Retorna False se a quantidade não é adequada
        """
        if quantidade_bebida.isdigit():
            quantidade_bebida = int(quantidade_bebida)
            return 1 <= quantidade_bebida <= 50
        return False

    def rodarInterface(self) -> None:
        # Cria a janela principal
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Cardápio de Bebidas")
        self.definirFundoTela('lightgray', self.root)
        self.criarWidgets(self.root)
        
        #maxima janela
        self.root.state('zoomed') 
        
        # Roda a interface
        self.root.mainloop()
        

# Inicializa a interface usando as bebidas importadas do módulo Lerbebidaexcel
interfaceCardapioBebidas = InterfaceCardapioBebidas(bebidas)
