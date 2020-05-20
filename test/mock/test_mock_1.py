# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:16:41 2020

@author: usuari
"""

import unittest
from src.Confirmar_reserva import Confirmar_Reserva
from requests.exceptions import Timeout
from unittest import mock

class TestMock1(unittest.TestCase):
    @mock.patch('src.Confirmar_Reserva.os.patch')
    @mock.patch('src.Confirmar_Reserva.os')
    def test_Confirmar_reserva(self, mock_Reserva):
        
        self.assertTrue(mock_Reserva.ConfirmacioReserva("Iberia","US-1"))
        mock_Reserva.ConfirmacioReserva(("Iberia","US-1")).return_value = False
        self.assertFalse(mock_Reserva.ConfirmacioReserva(("Iberia","US-1")))