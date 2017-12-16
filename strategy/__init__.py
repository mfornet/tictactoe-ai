from .random import RandomPlayer
from .montecarlo import MontecarloPlayer


PLAYER_NAMES = {
    'User' : (lambda game : None),
    'Random' : RandomPlayer,
    'Montecarlo' : MontecarloPlayer
}


def load_player(player_name):
    return PLAYER_NAMES[player_name]
