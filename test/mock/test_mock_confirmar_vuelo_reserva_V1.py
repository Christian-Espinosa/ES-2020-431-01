# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:16:41 2020

@author: usuari
"""
import os
import sys
import unittest
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
PROJECT_DIR = os.path.join(PROJECT_DIR, '..', 'src')
if not PROJECT_DIR is sys.path:
    sys.path.insert(0, PROJECT_DIR)

from Confirmar_reserva import Confirmar_Reserva
from requests.exceptions import Timeout
from unittest import mock

class TestMock1(unittest.TestCase):
    @mock.patch('Confirmar_reserva.os.path')
    def test_Confirmar_reserva(self, mock_Reserva):
        
        self.assertTrue(mock_Reserva.ConfirmacioReserva("Iberia","US-1"))