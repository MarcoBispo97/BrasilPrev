from abc import ABC, abstractmethod

from banco_imobiliario.config import settings


class JogadorBase(ABC):

    def __init__(
        self, estrategia, posicao=0,
        dinheiro=settings.ENV_Jogador_DINHEIRO
    ):
        self.posicao = posicao
        self.dinheiro = dinheiro
        self.estrategia = estrategia
        self.fimdejogo= False

    def __str__(self):
        return f"{self.estrategia}"

    def __repr__(self):
        return f"{self.estrategia}"

    def income_or_sale(self, patrimonio, tabuleiro=None):
        if patrimonio.type_of_estrategia:
            if self != patrimonio.type_of_estrategia:
                self.paid(patrimonio.rental_preco, patrimonio.type_of_estrategia)
            return

        if self._tipos_de_pagamento(patrimonio):
            patrimonio.type_of_estrategia = self

    @abstractmethod
    def _tipos_de_pagamento(self, patrimonio, tabuleiro):
        raise NotImplementedError()

    def paid(self, propriedade_preco, type_of_estrategia=None):
        self.dinheiro -= propriedade_preco
        if type_of_estrategia:
            type_of_estrategia.dinheiro += propriedade_preco
        if not self.dinheiro:
            self.fimdejogo= True
