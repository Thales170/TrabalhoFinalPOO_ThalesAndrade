"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Maio de 2024
"""
#importo essa biblioteca para conseguir ler arquivos do excel (extensão .xlsx)
import pandas as pd

class Sanduiche:
    def __init__(self, nome: str, descricao: str, preco: int) -> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        

# Função para ler os dados do arquivo Excel e criar objetos Sanduiche.
# Cada objeto poderá ser acessado através de um índice da lista sanduiches[].
# Ou seja, todos os objetos podem ser acessados através da variável sanduiches[]. Que nada mais é que um vetor, uma lista.
def ler_sanduiches(nome_arquivo: str) -> list:
    """
    Parâmentro: Recebe o nome do arquivo.xlsx que será acessado
    Retorna: uma variável do tipo lista, que guarda todos os sanduíches, com Nome, Descrição e Preço podendo ser acessadas.
    """
    dados_excel = pd.read_excel(nome_arquivo, header=None, skiprows=1)    #vai pular a primeira linha do arquivo Excel. Essa linha não tem informações importantes.
    sanduiches = []                 #variável que vai guardar cada um dos sanduiches, com sua respectiva descrição e preço.
    for index, row in dados_excel.iterrows():
        nome = row[0]                   #NOME está na primeira coluna
        descricao = row[1]              #DESCRIÇÃO está na segunda coluna
        preco = row[2]                  #PREÇO está na terceira coluna do excel.
        sanduiche = Sanduiche(nome, descricao, preco)       #Estou criando objetos da classe Sanduiche.
        sanduiches.append(sanduiche)
    return sanduiches                   #Terminou de ler todos os sanduiches.



arquivo_excel = r'C:\Users\dudua\OneDrive\Área de Trabalho\Área de Trabalho\UFMG_2024.1\POO\TrabalhoFinal\cardapioSanduiche.xlsx'  # Nome do arquivo Excel
sanduiches = ler_sanduiches(arquivo_excel)
