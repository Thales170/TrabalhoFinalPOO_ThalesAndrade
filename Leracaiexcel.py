"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Maio de 2024
"""
#importo essa biblioteca para conseguir ler arquivos do excel (extensão .xlsx)
import pandas as pd

class Acai:
    def __init__(self, descricao: str, preco: int) -> None:
        self.descricao = descricao
        self.preco = preco
        

# Função para ler os dados do arquivo Excel e criar objetos Acai.
# Cada objeto poderá ser acessado através de um índice da lista acais[].
# Ou seja, todos os objetos podem ser acessados através da variável acais[]. Que nada mais é que um vetor, uma lista.
def ler_acais(nome_arquivo: str) -> list:
    """
    Parâmentro: Recebe o nome do arquivo.xlsx que será acessado
    Retorna: uma variável do tipo lista, que guarda todos os sanduíches, com Descrição e Preço podendo ser acessadas.
    """
    
    dados_excel = pd.read_excel(nome_arquivo, header=None, skiprows=1)    #vai pular a primeira linha do arquivo Excel. Essa linha não tem informações importantes.Só o cabeçalho da tabela.
    acais = []                 #variável que vai guardar cada um dos açaís, com sua respectiva descrição e preço.
    for index, row in dados_excel.iterrows():
        descricao = row[0]              #DESCRIÇÃO está na primeira coluna
        preco = row[1]                  #PREÇO está na segunda coluna do excel.
        acai = Acai(descricao, preco)       #Estou criando objetos da classe Acai.
        acais.append(acai)
    return acais               #Terminou de ler todos os acais



arquivo_excel = r'C:\Users\dudua\OneDrive\Área de Trabalho\Área de Trabalho\UFMG_2024.1\POO\TrabalhoFinal\cardapioAcai.xlsx'  # Nome do arquivo Excel
acais = ler_acais(arquivo_excel)

