import os
import sys
import unittest

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
PROJECT_DIR = os.path.join(PROJECT_DIR, '..', 'src')
if not PROJECT_DIR is sys.path:
    sys.path.insert(0, PROJECT_DIR)

from Confirmar_reserva import Confirmar_Reserva



"""
Dado un viaje con múltiples destinos y más de un viajero, cuando se confirma
correctamente la reserva de los vuelos, se reporta que la acción se ha realizado
correctamente

"""


class TestConfirmarReservaVehiculos(unittest.TestCase):

    #def setUpClass(cls):
        #cls.


        """
        player1 = Player("player1")
        player2 = Player("player2")
        game = Game(player1, player2)

        score_max = max(score_player_1, score_player_2)
        for score in range(0, score_max):
            if score < score_player_1:
                game.won_point(player1)
            if score < score_player_2:
                game.won_point(player2)

        score = game.get_score()

        assert score == expected_result
        """
