from random import randint

from .base import JogadorBase


class JogadorAleatorio(JogadorBase):
    '''
    O jogador aleatório compra a propriedade
    que ele parar em cima com probabilidade
    de 50%.
    '''
    def _tipos_de_pagamento(self, patrimonio):
        if randint(0, 1) > 0:
            self.paid(patrimonio.propriedade_preco, patrimonio.type_of_estrategia)
            return True
        return False
