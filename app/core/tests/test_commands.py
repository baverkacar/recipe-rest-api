from importlib.resources import path
from token import OP
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError # throws error when database is not active
from django.test import TestCase

class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""

        """checking connection with patch using ConnectionHandler"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db') 
            self.assertEqual(gi.call_count, 1) # if call_count equals 1 it says dbase is active

    @patch('time.sleep', return_value = True) # decorator of waiting for a sec
    def test_wait_for_db(self,ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True] # first five times it will send a error
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
