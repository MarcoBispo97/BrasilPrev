from .base import JogadorBase


class JogadorExigente(JogadorBase):
    '''
    O jogador exigente compra qualquer
    propriedade, desde que o valor do aluguel
    dela seja maior do que 50.
    '''
    def _tipos_de_pagamento(self, patrimonio):
        if patrimonio.rental_preco > 50:
            self.paid(patrimonio.propriedade_preco, patrimonio.type_of_estrategia)
            return True
        return False
