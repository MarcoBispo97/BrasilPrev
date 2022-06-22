from banco_imobiliario.config import settings
from .game_tabuleiro import GameTabuleiro
from .jogador_cautelosoimport JogadorCauteloso
from .jogador_exigente import JogadorExigente
from .jogador_impulsivo import JogadorImpulsivo
from .jogador_aleatorio import JogadorAleatorio

estrategias = {
    "impulsivo": JogadorImpulsivo,
    "exigente": JogadorExigente,
    "cauteloso": JogadorCauteloso,
    "aleatorio": JogadorAleatorio,
}


def create_Jogador(estrategia: str, *args, **kwargs):
    try:
        return estrategias[estrategia](estrategia=estrategia, *args, **kwargs)

    except KeyError:
        available_estrategias = ", ".join(estrategias.keys())
        raise NotImplementedError(
            f"The Jogador estrategia '{estrategia}' is not implemented."
            f"Please use the available estrategias: {available_estrategias}"
        )


def create_tabuleiro():
    tabuleiro = GameTabuleiro()
    jogadores = [
        create_Jogador(estrategia)
        for estrategia in settings.ENV_ESTRATEGIA
    ]
    tabuleiro.jogadores = jogadores
    return tabuleiro
