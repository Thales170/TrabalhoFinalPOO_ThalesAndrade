"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

# Importa a classe abstrata do arquivo Interface
from interface import Interface

# Importa a classe responsável por montar/adicionar/remover itens no carrinho de compras.
from carrinhodecompras import carrinho

# Para a interface gráfica
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

class InterfaceCarrinhoDeCompras(Interface):
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
        titulo_fonte = tkfont.Font(family="Lucida Handwriting", size=20, weight="bold", slant="italic")
        titulo1 = tk.Label(root, text="Tribo do Thales", bg="lightgray", fg="navy", font=titulo_fonte) #navy = azul marinho
        titulo1.place(relx=0.05, y=30, anchor='nw')  # Posição do texto.

        # Título "CARRINHO DE COMPRAS"
        titulo2_fonte = tkfont.Font(family="Helvetica", size=20, weight="bold")
        titulo2 = tk.Label(root, text="CARRINHO DE COMPRAS", bg="lightgray", fg="darkred", font=titulo2_fonte)
        titulo2.place(relx=0.5, y=20, anchor='n')

        # Frame para a LISTA DE ITENS.
        frame_lista = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
        frame_lista.place(relwidth=0.50, relheight=0.75, relx=0.02, rely=0.15)

        # Criar a tabela de itens no frame_lista
        self.criarTabela(frame_lista)
        
        # Cria texto Valor Total
        self.label_valortotal = tk.Label(root, text=f"Valor total: R${carrinho.calcularTotal():.2f}", bg="lightgray", fg="black", font=("Arial", 14))
        self.label_valortotal.place(relx=0.76, rely=0.85)
        
        # Frame para o endereço
        frame_endereco = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
        frame_endereco.place(relwidth=0.40, relheight=0.35, relx=0.55, rely=0.15)
        
        # Adiciona os campos de endereço no frame_endereco
        self.criarCamposEndereco(frame_endereco)

        # Botão "FINALIZAR"
        btn_proximo = tk.Button(root,bg="LimeGreen",text="FINALIZAR COMPRA",font=("Helvetica", 10, "bold"), command=self.finalizarCompra)
        btn_proximo.place(relx=0.77, rely=0.9)

        # Botão "VOLTAR"
        btn_voltar = tk.Button(root, text="ADICIONAR MAIS PRODUTOS", command=self.botaoVoltar)
        btn_voltar.place(relx=0.02, rely=0.95)
        
    def criarCamposEndereco(self, frame) -> None:
        """
        Parâmetro frame: recebe os dados de posição/cor/tamanho do frame criado. Da "caixa/ seção" criada.
        """
        # Inicializando as StringVars dentro do método criarCamposEndereco
        self.bairro = tk.StringVar()
        self.rua = tk.StringVar()
        self.numero = tk.StringVar()
        self.complemento = tk.StringVar()
        
        # Rótulo e campo "Bairro"
        tk.Label(frame, text="Bairro:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        entry_bairro = tk.Entry(frame, textvariable=self.bairro)
        entry_bairro.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Rótulo e campo "Rua"
        tk.Label(frame, text="Rua:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        entry_rua = tk.Entry(frame, textvariable=self.rua)
        entry_rua.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Rótulo e campo "Número"
        tk.Label(frame, text="Número:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        entry_numero = tk.Entry(frame, textvariable=self.numero)
        entry_numero.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # Rótulo e campo "Complemento"
        tk.Label(frame, text="Complemento/informações extras de localização:", bg="white").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        entry_complemento = tk.Entry(frame, textvariable=self.complemento)
        entry_complemento.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    def criarTabela(self, frame)-> None:
        """
        Parâmetro frame: recebe os dados de posição/cor/tamanho do frame criado. Da "caixa/ seção" criada.
        """
        # Cabeçalhos da tabela
        header_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        tk.Label(frame, text="Quantidade", bg="lightgray", font=header_font).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(frame, text="Descrição", bg="lightgray", font=header_font).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame, text="Preço unit.", bg="lightgray", font=header_font).grid(row=0, column=2, padx=10, pady=5)
        tk.Label(frame, text="Remover", bg="lightgray", font=header_font).grid(row=0, column=3, padx=10, pady=5)

        # Itens do carrinho
        for i, item in enumerate(carrinho.itens):
            tk.Label(frame, text=item['quantidade'], bg="lightgray").grid(row=i+1, column=0, padx=10, pady=5)
            tk.Label(frame, text=item['descricao'], bg="lightgray").grid(row=i+1, column=1, padx=10, pady=5)
            tk.Label(frame, text=f"R${item['preco']:.2f}", bg="lightgray").grid(row=i+1, column=2, padx=10, pady=5)
            btn_remover = tk.Button(frame,bg="PaleVioletRed", text="Remover",font=("Helvetica", 10, "bold"), command=lambda index=i: self.removerItem(index))
            btn_remover.grid(row=i+1, column=3, padx=10, pady=5)
     
    # Função para tirar item da lista carrinho, e chamar a função de atualizar interface.
    def removerItem(self, index:int) -> None:
        """
        Parâmetro index: recebe o índice da lista que será removido.
        """
        carrinho.removerItem(index)
        self.atualizarInterface()
    
    # Função que vai apagar as informações antigas e atualizar para as novas. Tipo um F5.
    def atualizarInterface(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.criarWidgets(self.root)

    def botaoVoltar(self):
        # FECHA ESSA INTERFACE
        self.root.destroy()

        # Importa a interface anterior, caso aperte o botão voltar, vai retornar para essa interface. Importei o objeto instanciado.
        from interfaceInicio import interface_inicio

        # VOLTAR PARA A INTERFACE DO MENU PRINCIPAL
        interface_inicio.rodarInterface()

    def finalizarCompra(self):
        # Validação dos campos
        if not self.validarBairro():
            messagebox.showerror("Erro", "O campo 'Bairro' deve conter pelo menos uma palavra e não deve conter números.")
            return

        if not self.validarRua():
            messagebox.showerror("Erro", "O campo 'Rua' deve conter pelo menos uma palavra e não deve conter números.")
            return

        if not self.validarNumero():
            messagebox.showerror("Erro", "O campo 'Número' deve conter apenas números.")
            return

        self.registraPedido()        

        # FECHA ESSA INTERFACE
        self.root.destroy()
        
        
    def registraPedido(self):
        # Nome do arquivo onde será registrado o pedido
        nome_arquivo = "pedido.txt"
        
        # Abrindo o arquivo para escrita, modo append
        with open(nome_arquivo, 'a') as arquivo:
            # Escrevendo os itens do carrinho
            arquivo.write("ITENS DO CARRINHO:\n")
            for item in carrinho.itens:
                arquivo.write(f"Quantidade: {item['quantidade']}, Descrição: {item['descricao']}, Preço: R${item['preco']:.2f}\n")
                
            arquivo.write(f"\nValor total: R${carrinho.calcularTotal():.2f}")

            # Escrevendo o endereço de entrega
            arquivo.write("\n\nENDEREÇO DE ENTREGA:\n")
            arquivo.write(f"Bairro: {self.bairro.get()}\n")
            arquivo.write(f"Rua: {self.rua.get()}\n")
            arquivo.write(f"Número: {self.numero.get()}\n")
            arquivo.write(f"Complemento: {self.complemento.get()}\n\n\n\n")
            
            

        # Mensagem de confirmação
        messagebox.showinfo("Pedido Registrado", "Pedido registrado com sucesso!\n"
           "Seu pedido será entregue dentro de 1h:30min\n"
           "Formas de pagamento: Dinheiro, Pix, Débito e Crédito")
        
        
        

    def validarBairro(self):
        """
        Retorna True se bairro é adequado. Não digitou nenhum número.
        Se não, retorna False.
        """    
        bairro = self.bairro.get().strip()
        return bool(bairro) and not any(char.isdigit() for char in bairro)

    def validarRua(self):
        """
        Retorna True se rua é adequada. Não digitou nenhum número.
        Se não, retorna False.
        """ 
#.strip(): Remove quaisquer espaços em branco no início e no final da string. Isso garante que uma entrada como " Rua ABC " seja transformada em "Rua ABC".        
        rua = self.rua.get().strip() 
        return bool(rua) and not any(char.isdigit() for char in rua)
#bool(rua) converte string em Booleana. Se campo estiver vazio, já gera 0. Se colocar qualquer coisa no campo rua, gera 1.

    def validarNumero(self):
        numero = self.numero.get().strip()
        return numero.isdigit()
        
        

    def rodarInterface(self) -> None:
        # Cria a janela principal
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Carrinho de Compras")
        self.definirFundoTela('lightgray', self.root)
        self.criarWidgets(self.root)
        

        # Maximiza a janela
        self.root.state('zoomed')

        # Roda a interface
        self.root.mainloop()

# Inicializa a interface do carrinho de compras
interfaceCarrinho = InterfaceCarrinhoDeCompras()

