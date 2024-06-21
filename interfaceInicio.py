"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

# Importa a classe abstrata do arquivo Interface
from interface import Interface

# Importa interface de Pizzas, de Sanduiches, de Acai e de Bebidas, possíveis interfaces depois dessa interface inicial.
from interfaceCardapioPizzas import interfaceCardapioPizzas  #objeto da classe InterfaceCardapioPizzas.
from interfaceCardapioSanduiches import interfaceCardapioSanduiches
from interfaceCardapioAcai import interfaceCardapioAcai
from interfaceCardapioBebidas import interfaceCardapioBebidas
from interfaceCarrinhoDeCompras import interfaceCarrinho
from carrinhodecompras import carrinho

# Para a interface gráfica
import tkinter as tk
from tkinter import font as tkfont

class InterfaceInicio(Interface):
    def __init__(self):
        self.root = None

    def definirFundoTela(self, cor: str, root: tk.Tk) -> None:
        """
        Parâmetro cor: recebe a cor de background da tela/guia
        Parâmetro root: recebe a guia/tela que será editada e exibida
        """
        root.configure(bg=cor)

    def criarWidgets(self, root: tk.Tk) -> None:
        """
        Parâmetro root: recebe a guia/tela que será editada e exibida
        """
        # Título "Tribo do Thales"
        titulo_fonte = tkfont.Font(family="Lucida Handwriting", size=35, weight="bold", slant="italic")
        titulo1 = tk.Label(root, text="Tribo do Thales", bg="lightgray", fg="navy", font=titulo_fonte)
        titulo1.place(relx=0.5, rely=0.05, anchor='n')

       

        # Frame para os botões
        frame_botoes = tk.Frame(root, bg="white")
        frame_botoes.place(relx=0.5, rely=0.30, anchor='n')

         # Texto "O quê deseja escolher?"
        texto_fonte = tkfont.Font(family="Arial", size=15)
        texto = tk.Label(root, text="O quê deseja escolher?", bg="lightgray", fg="black", font=texto_fonte)
        texto.place(relx=0.5, rely=0.23, anchor='n')

        # Botões
        fonte_botao = tkfont.Font(family="Marker Felt", size=12, weight="bold")
        btn_pizza = tk.Button(frame_botoes, text="Pizza", command=self.irParaPizza, width=40, height=5,bg="green",fg="white",font=fonte_botao)
        btn_pizza.grid(row=0, column=0, pady=(0, 1))

        btn_sanduiche = tk.Button(frame_botoes, text="SANDUICHE", command=self.irParaSanduiche, width=40, height=5,bg="green",fg="white",font=fonte_botao)
        btn_sanduiche.grid(row=1, column=0, pady=(0, 1))

        btn_acai = tk.Button(frame_botoes, text="AÇAI", command=self.irParaAcai, width=40, height=5,bg="green",fg="white",font=fonte_botao)
        btn_acai.grid(row=2, column=0, pady=(0, 1))

        btn_bebida = tk.Button(frame_botoes, text="BEBIDA", command=self.irParaBebida, width=40, height=5,bg="green",fg="white",font=fonte_botao)
        btn_bebida.grid(row=3, column=0, pady=(0, 1))
        
        # Condição para exibir o botão "FINALIZAR PEDIDO"
        if len(carrinho.itens) >= 1:
            btn_carrinho_de_compras = tk.Button(root, text="FINALIZAR PEDIDO", command=self.irParaCarrinhoDeCompras, height=2, bg="darkred", fg="white", font=fonte_botao)
            btn_carrinho_de_compras.pack(side=tk.BOTTOM, fill=tk.X)
        
        #ESTOU MEXENDO AQUI ADICIONANDO O BOTÃ FINALZIAR PEDIDO
        
    def irParaPizza(self)-> None:
        #VOU FECHAR ESSA INTERFACE 
        self.root.destroy()
        
        #VOU ABRIR A INTERFACE DO CARDAPIO DE PIZZAS
        interfaceCardapioPizzas.rodarInterface( )
        
    def irParaSanduiche(self)-> None:
        #VOU FECHAR ESSA INTERFACE 
        self.root.destroy()
        
        #VOU ABRIR A INTERFACE DO CARDAPIO DE PIZZAS
        interfaceCardapioSanduiches.rodarInterface( )
        
    def irParaAcai(self)-> None:
        #VOU FECHAR ESSA INTERFACE 
        self.root.destroy()
        
        #VOU ABRIR A INTERFACE DO CARDAPIO DE PIZZAS
        interfaceCardapioAcai.rodarInterface( )
    
    def irParaBebida(self)-> None:
        #VOU FECHAR ESSA INTERFACE 
        self.root.destroy()
        
        #VOU ABRIR A INTERFACE DO CARDAPIO DE PIZZAS
        interfaceCardapioBebidas.rodarInterface( )
    
    def irParaCarrinhoDeCompras(self)->None:
        #VOU FECHAR ESSA INTERFACE 
        self.root.destroy()
        
        #VOU ABRIR A INTERFACE DO CARRINHO DE COMPRAS
        interfaceCarrinho.rodarInterface( )
        

    def rodarInterface(self) -> None:
        # Cria a janela principal
        self.root = tk.Tk()
        self.root.title("Escolha do Pedido")
        self.definirFundoTela('lightgray', self.root)
        self.criarWidgets(self.root)
        
        #maxima janela
        self.root.state('zoomed') 

        # Roda a interface
        self.root.mainloop()

# Inicializa a interface de início

interface_inicio = InterfaceInicio()
