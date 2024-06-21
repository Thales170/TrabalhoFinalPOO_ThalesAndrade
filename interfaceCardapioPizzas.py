"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

# Importa a variável pizzas do arquivo em python Lerpizzaexcel.py
from Lerpizzaexcel import pizzas as pizzas_excel

# Importa a classe abstrata do arquivo Interface
from interface import Interface

#Importa a classe responsável por montar/adicionar/remover itens no carrinho de compras.
from carrinhodecompras import carrinho

# Para a interface gráfica
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

# Define os preços das pizzas
preco_pizzaP = 26.00
preco_pizzaM = 42.00
preco_pizzaG = 60.00

class InterfaceCardapioPizzas(Interface):
    def __init__(self, pizzas):
        self.pizzas = pizzas
        self.root = None

    def definirFundoTela(self, cor: str, root: tk.Tk) -> None:
        """
        Parâmetro cor: recebe a cor de fundo da tela
        Parâmetro root: recebe a guia/janela que será editada
        """
        root.configure(bg=cor)

    def criarWidgets(self, root: tk.Tk) -> None:
        """
        Parâmetro root: recebe a guia/janela que será editada.
        """
        # Título "Tribo do Thales"
        titulo_fonte = tkfont.Font(family="Lucida Handwriting", size=20, weight="bold", slant="italic")
        titulo1 = tk.Label(root, text="Tribo do Thales", bg="lightgray", fg="navy", font=titulo_fonte) #navy = azul marinho
        titulo1.place(relx=0.05, y=30, anchor='nw')          #Posição do texto.

        # Título "CARDÁPIO DE PIZZAS"
        titulo2_fonte = tkfont.Font(family="Helvetica", size=20, weight="bold")
        titulo2 = tk.Label(root, text="CARDÁPIO DE PIZZAS", bg="lightgray", fg="darkred", font=titulo2_fonte)
        titulo2.place(relx=0.5, y=20, anchor='n')

        # Frame para a lista de pizzas
        frame_pizzas = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
        frame_pizzas.place(relwidth=0.5, relheight=0.77, relx=0.05, rely=0.15)

        # Exibir as pizzas
        for i, pizza in enumerate(self.pizzas):
            pizza_label = tk.Label(frame_pizzas, text=f"{i + 1}. {pizza.sabor}", bg="lightgray", fg="black", font=("Helvetica", 11, "bold"))
            pizza_label.pack(anchor='w', padx=10, pady=(5, 0))

            descricao_label = tk.Label(frame_pizzas, text=pizza.descricao, bg="lightgray", fg="black", font=("Times New Roman", 10))
            descricao_label.pack(anchor='w', padx=20, pady=(0, 5))
            
            
        # Frame para a lista de preços
        frame_preco = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
        frame_preco.place(relwidth=0.13, relheight=0.16, relx=0.64, rely=0.55)
        
        # Exibe lista de preços
        preco_label1 = tk.Label(frame_preco, text=f"Pequena (P): R${preco_pizzaP:.2f}", bg="lightgray", fg="black", font=("Helvetica", 11, "bold"))
        preco_label1.pack(anchor='w', padx=10, pady=5)
        preco_label2 = tk.Label(frame_preco, text=f"Média (M): R${preco_pizzaM:.2f}", bg="lightgray", fg="black", font=("Helvetica", 11, "bold"))
        preco_label2.pack(anchor='w', padx=10, pady=5)
        preco_label3 = tk.Label(frame_preco, text=f"Grande (G): R${preco_pizzaG:.2f}", bg="lightgray", fg="black", font=("Helvetica", 11, "bold"))
        preco_label3.pack(anchor='w', padx=10, pady=5)

        # Caixa de diálogo para NUMERO DA PIZZA
        dialog_frame = tk.Frame(root, bg="lightgray")
        dialog_frame.place(relwidth=0.2, relheight=0.2, relx=0.6, rely=0.15)

        # Mensagem para o usuário
        msg_label = tk.Label(dialog_frame, text="Digite o número correspondente à pizza selecionada", bg="lightgray", fg="black")
        msg_label.pack(pady=5)

        self.entry_pizza_num = tk.Entry(dialog_frame, bg="white", fg="black")
        self.entry_pizza_num.pack(pady=5)
        
        # Caixa de diálogo para TAMANHO DA PIZZA
        dialog_frame3 = tk.Frame(root, bg="lightgray")
        dialog_frame3.place(relwidth=0.2, relheight=0.2, relx=0.6, rely=0.25)

        # Mensagem para o usuário
        msg_label3 = tk.Label(dialog_frame3, text="Tamanho da pizza: (P,M,G)", bg="lightgray", fg="black")
        msg_label3.pack(pady=5)

        self.entry_pizza_tamanho = tk.Entry(dialog_frame3, bg="white", fg="black")
        self.entry_pizza_tamanho.pack(pady=5)

        # Caixa de diálogo para QUANTIDADE DE PIZZAS
        dialog_frame2 = tk.Frame(root, bg="lightgray")
        dialog_frame2.place(relwidth=0.2, relheight=0.2, relx=0.6, rely=0.35)

        # Mensagem para o usuário
        msg_label2 = tk.Label(dialog_frame2, text="Quantidade", bg="lightgray", fg="black")
        msg_label2.pack(pady=5)

        self.entry_pizza_quantidade = tk.Entry(dialog_frame2, bg="white", fg="black")
        self.entry_pizza_quantidade.pack(pady=5)

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
        num_pizza = self.entry_pizza_num.get()
        tamanho_pizza = self.entry_pizza_tamanho.get().upper()
        quantidade_pizza = self.entry_pizza_quantidade.get()

        if not self.validarValorDigitado(num_pizza):
            messagebox.showerror("Erro", f"Escolha uma pizza de 1 até {len(self.pizzas)}.")
        elif not self.validarTamanhoDigitado(tamanho_pizza):
            messagebox.showerror("Erro", "Tamanho de pizza, inválido. Escolha entre 'P', 'M' ou 'G'.")
        elif not self.validarQuantidadeDigitada(quantidade_pizza):
            messagebox.showerror("Erro", "Quantidade de pizzas não permitida. Favor insira um número de 1 a 50.")
        else:
            num_pizza = int(num_pizza)
            quantidade_pizza = int(quantidade_pizza)
            pizza = self.pizzas[num_pizza-1]
            
            # Determinar o preço com base no tamanho da pizza
            if tamanho_pizza == 'P':
                preco_pizza = preco_pizzaP
            elif tamanho_pizza == 'M':
                preco_pizza = preco_pizzaM
            else:  # Tamanho 'G'
                preco_pizza = preco_pizzaG
            
            carrinho.addItem ({
                'descricao': pizza.sabor,
                'preco': preco_pizza,
                'quantidade': quantidade_pizza
            })
            
            messagebox.showinfo("Seleção", f"Você selecionou a pizza {self.pizzas[num_pizza - 1].sabor}.\nTamanho: {tamanho_pizza}\nQuantidade: {quantidade_pizza}.")
            
            #FECHO ESSA JANELA
            
            self.root.destroy()
            from interfaceInicio import interface_inicio
                
            #VOU VOLTAR PARA A INTERFACE DO MENU PRINCIPAL
            interface_inicio.rodarInterface( )
            

    def validarValorDigitado(self, num_pizza):
        """
        Parâmetro num_pizza: recebe o número da pizza digitado pelo usuário
        Retorna True se o numero digitado é adequada, Retorna False se o valor digitado não é adequada
        """
        if num_pizza.isdigit():
            num_pizza = int(num_pizza)
            return 1 <= num_pizza <= len(self.pizzas)
        return False

    def validarTamanhoDigitado(self, tamanho_pizza):
        """
        Parâmetro tamanho_pizza: recebe o tamanho da pizza digitado pelo usuário
        Retorna True se o tamanho digitado é adequada, Retorna False se o tamanho não é adequado
        """
        return tamanho_pizza in ['P', 'M', 'G']

    def validarQuantidadeDigitada(self, quantidade_pizza):
        """
        Parâmetro quantidade_pizza: recebe a quantidade de pizzas digitado pelo usuário
        Retorna True se o numero digitado é adequada, Retorna False se a quantidade não é adequada
        """
        if quantidade_pizza.isdigit():
            quantidade_pizza = int(quantidade_pizza)
            return 1 <= quantidade_pizza <= 50
        return False
    
    def rodarInterface(self) -> None:
        # Cria a janela principal
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Cardápio de Pizzas")
        self.definirFundoTela('lightgray', self.root)
        self.criarWidgets(self.root)

        #maxima janela
        self.root.state('zoomed') 

        # Roda a interface
        self.root.mainloop()

# Inicializa a interface usando as pizzas importadas do módulo Lerpizzaexcel
interfaceCardapioPizzas = InterfaceCardapioPizzas(pizzas_excel)



