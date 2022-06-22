from datetime import datetime
from random import randint

from banco_imobiliario.config import settings

from .card_patrimonio import Patrimonio


class GameTabuleiro:

    def __init__(self, *args, **kwargs):
        self._vencedor = None
        self._played = 0
        self._jogadores = []
        self.start_time = datetime.now()
        self._cards = [
            Patrimonio(index, None)
            for index in range(
                int(settings.ENV_QUANTIDADE_DE_PROPRIEDADES)
            )
        ]

    @propriedade
    def played(self):
        return self._played

    @played.setter
    def played(self, played):
        self._played = played

    @propriedade
    def jogadores(self):
        return self._jogadores

    @jogadores.setter
    def jogadores(self, jogadores):
        self._jogadores = jogadores

    @propriedade
    def vencedor(self):
        return self._vencedor

    @vencedor.setter
    def vencedor(self, vencedor):
        self._vencedor = vencedor

    @propriedade
    def play_dice(self):
        '''
        No começo da sua vez, o jogador joga um
        dado equiprovável de 6 faces que determina
        quantas espaços no tabuleiro o jogador vai
        andar.
        '''
        return randint(1, 6)

    def __getitem__(self, posicao):
        return self._cards[posicao]

    def __setitem__(self, posicao, patrimonio):
        self._cards[posicao] = patrimonio

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"{self._cards}"

    def __repr__(self):
        return f"{self._cards}"

    def remove(self, Jogador):
        for patrimonio in self._cards:
            if patrimonio.type_of_estrategia == Jogador:
                patrimonio.type_of_estrategia = None
        self._jogadores.remove(Jogador)

    def walk(self, Jogador, _dice=None):
        go_to_posicao = Jogador.posicao + (_dice or self.play_dice)
        if go_to_posicao >= int(settings.ENV_QUANTIDADE_DE_PROPRIEDADES):
            '''
            Ao completar uma volta no tabuleiro,
            o jogador ganha 100 de saldo.
            '''
            Jogador.dinheiro += float(settings.ENV_Jogador_DINHEIRO_PARTIDA)
            go_to_posicao -= int(settings.ENV_QUANTIDADE_DE_PROPRIEDADES)
        Jogador.posicao = go_to_posicao
        return go_to_posicao

    def check_vencedor(self, Jogador):
        '''
        Termina quando restar somente um jogador
        com saldo positivo, a qualquer momento da
        partida. Esse jogador é declarado o
        vencedor.
        '''
        if len(self.jogadores) == 1:
            return Jogador
        if int(settings.ENV_FIM_DO_TEMPO_PARTIDA) <= self.played:
            dinheiro = 0
            vencedor = None
            for _Jogador in self._jogadores:
                if _Jogador.dinheiro > dinheiro:
                    dinheiro = _Jogador.dinheiro
                    vencedor = _Jogador
            return vencedor

        elements = [
            _Jogador.dinheiro
            for _Jogador in self._jogadores if _Jogador != Jogador
        ]
        if sum(elements) < 0:
            return Jogador

        return None

    def play(self, Jogador, tabuleiro):
        '''
        Um jogador que fica com saldo negativo
        perde o jogo, e não joga mais. Perde
        suas propriedades e portanto podem ser
        compradas por qualquer outro jogador.
        '''
        if Jogador.dinheiro <= 0:
            Jogador.fimdejogo= True
            return

        patrimonio = self._cards[self.walk(Jogador)]
        Jogador.income_or_sale(patrimonio, tabuleiro)

    def finish(self):
        return {
            "time_it": (datetime.now() - self.start_time).total_seconds(),
            "vencedor": self.vencedor,
            "dinheiro": self.vencedor.dinheiro,
            "played": self.played,
            "estrategia": self.vencedor,
            "time_out": self.played > int(settings.ENV_FIM_DO_TEMPO_PARTIDA),
        }
