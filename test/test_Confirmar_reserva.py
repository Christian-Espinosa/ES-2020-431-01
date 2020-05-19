#import pytest
import unittest

from Confirmar_reserva import Confirmar_Reserva
from unittest import mock
#from Confirmar_reserva import ConfirmacioReserva


"""
Dado un viaje con múltiples destinos y más de un viajero, cuando se confirma
correctamente la reserva de los vuelos, se reporta que la acción se ha realizado
correctamente

"""
"""
@pytest.mark.parametrize("score_player_1, score_player_2, expected_result", [
    (0, 0, "Love-All"),
    # (1, 1, "Fifteen-All"),
    # (2, 2, "Thirty-All"),
    # (3, 3, "Deuce"),
    # (4, 4, "Deuce"),
    # (1, 0, "Fifteen-Love"),
    # (0, 1, "Love-Fifteen"),
    # (2, 0, "Thirty-Love"),
    # (0, 2, "Love-Thirty"),
    # (3, 0, "Forty-Love"),
    # (0, 3, "Love-Forty"),
    # (4, 0, "Win for player1"),
    # (0, 4, "Win for player2"),
    # (2, 1, "Thirty-Fifteen"),
    # (1, 2, "Fifteen-Thirty"),
    # (3, 1, "Forty-Fifteen"),
    # (1, 3, "Fifteen-Forty"),
    # (4, 1, "Win for player1"),
    # (1, 4, "Win for player2"),
    # (3, 2, "Forty-Thirty"),
    # (2, 3, "Thirty-Forty"),
    # (4, 2, "Win for player1"),
    # (2, 4, "Win for player2"),
    # (4, 3, "Advantage player1"),
    # (3, 4, "Advantage player2"),
    # (5, 4, "Advantage player1"),
    # (4, 5, "Advantage player2"),
    # (15, 14, "Advantage player1"),
    # (14, 15, "Advantage player2"),
    # (6, 4, "Win for player1"),
    # (4, 6, "Win for player2"),
    # (16, 14, "Win for player1"),
    # (14, 16, "Win for player2"),
])
"""
class TestConfirmar(unittest.TestCase):
    @mock.patch("Confirmar_reserva.ConfirmacioReserva")
    def test_Confirmar_reserva(self, mock_Reserva):
        
        self.assertTrue(mock_Reserva.ConfirmacioReserva("Iberia","US-1"))
        mock_Reserva.ConfirmacioReserva(("Iberia","US-1")).return_value = False
        self.assertFalse(mock_Reserva.ConfirmacioReserva(("Iberia","US-1")))
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