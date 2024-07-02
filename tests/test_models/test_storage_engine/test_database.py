#!/usr/bin/python3
"""
Defines the unitteset for DataBase for Easy Freight.
"""

import unittest
from unittest.mock import patch
import models
from models.base_model import BaseModel
from models.storage_engine.database import DataBase
from models.carrier import Carrier
from models.userport Shipper
from models.shipment import Shipment
from models.offer import Offer
from models.vehicle import Vehicle
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class TestDataBase(unittest.TestCase):

    @patch('database.create_engine')
    def setUp(self, mock_create_engine):
        """Mock the database engine creation."""
        self.database = DataBase()

    def test_init(self):
        """Test database initialization."""
        self.assertIsNotNone(self.database._DataBase__engine)

    @patch('database.scoped_session')
    def test_reload(self, mock_scoped_session):
        """Test reloading the database session."""
        self.database.reload()
        mock_scoped_session.assert_called_once()

    def test_new_save_delete(self):
        """Test adding, saving, and deleting an object."""
        with patch.object(self.database._DataBase__session, 'add') as mock_add, \
             patch.object(self.database._DataBase__session, 'commit') as mock_commit, \
             patch.object(self.database._DataBase__session, 'delete') as mock_delete:
            obj = classes['Carrier']()  # Example object
            self.database.new(obj)
            mock_add.assert_called_with(obj)
            self.database.save()
            mock_commit.assert_called_once()
            self.database.delete(obj)
            mock_delete.assert_called_with(obj)

    def test_all(self):
        """Test querying all objects."""
        with patch.object(self.database._DataBase__session, 'query') as mock_query:
            self.database.all('Carrier')
            mock_query.assert_called_once()

    def test_get(self):
        """Test getting an object by class and ID."""
        with patch('models.storage.all', return_value={'Carrier.1': 'mock_carrier'}):
            result = self.database.get('Carrier', '1')
            self.assertEqual(result, 'mock_carrier')

    def test_count(self):
        """Test counting objects."""
        with patch('models.storage.all', return_value={'Carrier.1': 'mock_carrier', 'Carrier.2': 'mock_carrier2'}):
            count = self.database.count('Carrier')
            self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()