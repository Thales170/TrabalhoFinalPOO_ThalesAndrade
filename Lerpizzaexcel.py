"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Maio de 2024
"""
#importo essa biblioteca para conseguir ler arquivos do excel (extensão .xlsx)
import pandas as pd

class Pizza:
    def __init__(self,sabor:str, descricao: str) -> None:
        self.sabor = sabor
        self.descricao = descricao
        

# Função para ler os dados do arquivo Excel e criar objetos Pizza.
# Cada objeto poderá ser acessado através de um índice da lista pizzas[].
# Ou seja, todos os objetos podem ser acessados através da variável pizzas[]. Que nada mais é que um vetor, uma lista.
def ler_pizzas(nome_arquivo: str) -> list:
    """
    Parâmentro: Recebe o nome do arquivo.xlsx que será acessado
    Retorna: uma variável do tipo lista, que guarda todas pizzas, com Sabor, e Descrição podendo ser acessadas.
    """
    dados_excel = pd.read_excel(nome_arquivo, header=None, skiprows=1)    #vai pular a primeira linha do arquivo Excel. Essa linha não tem informações importantes. Só o cabeçalho da tabela.
    pizzas = []                 #variável que vai guardar cada uma das pizzas, com sua respectiva descrição.
    for index, row in dados_excel.iterrows():
        sabor = row[0]                   #SABOR está na primeira coluna
        descricao = row[1]              #DESCRIÇÃO está na segunda coluna
        pizza = Pizza(sabor, descricao)       #Estou criando objetos da classe Pizza.
        pizzas.append(pizza)
    return pizzas                  #Terminou de ler todos as pizzas.



"""
FUNÇÃO UTILIZADA ANTES DE IMPLEMENTAR INTERFACE GRÁFICA, IRIA EXIBIR NO PROMPT DE COMANDO
def mostrarMenu(pizzas) -> None:   #Recebe a lista pizzas, que contém Todas variáveis do tipo Pizza. 
    print("\n                                  CARDÁPIO DE PIZZAS")
    print("-------------------------------------------------------------------------------------------------------------------------")
    quantidade_pizzas = len(pizzas)        
    for i in range(quantidade_pizzas):     #fiz um LAÇO FOR que vai percorrer todos os itens dessa lista. De 0 até o máximo de elementos
        print("| [",i+1,"]",pizzas[i].sabor.upper())
        print("|",pizzas[i].descricao)
        print("-------------------------------------------------------------------------------------------------------------------------")
  
"""

arquivo_excel = r'C:\Users\dudua\OneDrive\Área de Trabalho\Área de Trabalho\UFMG_2024.1\POO\TrabalhoFinal\cardapioPizza.xlsx'  # Nome do arquivo Excel
pizzas = ler_pizzas(arquivo_excel)   #todas as pizzas contidas na tabela excel vão para a variável pizzas.

# Exibindo o Menu de sanduiches
#mostrarMenu(pizzas)