"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""
#Estou criando essa classe abstrata para mostrar os métodos que suas subclasses obrigatoriamente devem ter.

from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def definirFundoTela(self, cor: str)-> None:
        pass

    def criarWidgets(self) -> None:
        pass

    def rodarInterface(self)->None:
        pass
