"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Maio de 2024
"""
#importo essa biblioteca para conseguir ler arquivos do excel (extensão .xlsx)
import pandas as pd

class Bebida:
    def __init__(self, descricao: str, preco: int) -> None:
        self.descricao = descricao
        self.preco = preco
        

# Função para ler os dados do arquivo Excel e criar objetos Bebida.
# Cada objeto poderá ser acessado através de um índice da lista bebidas[].
# Ou seja, todos os objetos podem ser acessados através da variável bebidas[]. Que nada mais é que um vetor, uma lista.
def ler_bebidas(nome_arquivo: str) -> list:
    """
    Parâmentro: Recebe o nome do arquivo.xlsx que será acessado
    Retorna: uma variável do tipo lista, que guarda todos as bebidas, com Descrição e Preço podendo ser acessadas.
    """
    
    dados_excel = pd.read_excel(nome_arquivo, header=None, skiprows=1)    #vai pular a primeira linha do arquivo Excel. Essa linha não tem informações importantes.Só o cabeçalho da tabela.
    bebidas = []                 #variável que vai guardar cada uma das bebidas, com sua respectiva descrição e preço.
    for index, row in dados_excel.iterrows():
        descricao = row[0]              #DESCRIÇÃO está na primeira coluna
        preco = row[1]                  #PREÇO está na segunda coluna do excel.
        bebida = Bebida(descricao, preco)       #Estou criando objetos da classe Bebida.
        bebidas.append(bebida)
    return bebidas               #Terminou de ler todos as bebidas

  

arquivo_excel = r'C:\Users\dudua\OneDrive\Área de Trabalho\Área de Trabalho\UFMG_2024.1\POO\TrabalhoFinal\cardapioBebida.xlsx'  # Nome do arquivo Excel
bebidas = ler_bebidas(arquivo_excel)
