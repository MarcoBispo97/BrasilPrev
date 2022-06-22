from .base import JogadorBase


class JogadorCauteloso(JogadorBase):
    '''
    O jogador cauteloso compra qualquer
    propriedade desde que ele tenha uma
    reserva de 80 saldo sobrando
    depois de realizada a compra.
    '''
    def _tipos_de_pagamento(self, patrimonio):
        if (self.dinheiro - patrimonio.propriedade_preco) >= 80:
            self.paid(patrimonio.propriedade_preco, patrimonio.type_of_estrategia)
            return True
        return False
