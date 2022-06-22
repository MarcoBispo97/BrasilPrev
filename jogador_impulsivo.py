from .base import JogadorBase


class JogadorImpulsivo(JogadorBase):
    '''
    O jogador impulsivo compra qualquer
    propriedade sobre a qual ele parar.
    '''
    def _tipos_de_pagamento(self, patrimonio):
        self.paid(patrimonio.propriedade_preco, patrimonio.type_of_estrategia)
        return True
