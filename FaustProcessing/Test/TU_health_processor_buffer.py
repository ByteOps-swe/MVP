import unittest
from ..HealthStateModel.health_processor_buffer import health_processor_buffer
from unittest.mock import MagicMock
from ..HealthStateModel.lista_misurazioni import lista_misurazioni

class TestHealthProcessorBuffer(unittest.TestCase):

    def setUp(self):
        self.health_processor = health_processor_buffer()

    def test_add_misurazione(self):
        # Mocking the lista_misurazioni instance
        mock_lista_misurazioni = MagicMock()
        self.health_processor._health_processor_buffer__lista_misurazioni = mock_lista_misurazioni

        # Test data
        timestamp = "2024-03-28 10:00:00"
        value = 25.5
        type_ = "Temperature"
        latitude = 37.7749
        longitude = -122.4194
        ID_sensore = "ABC123"
        cella = "A1"

        # Call method under test
        self.health_processor.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

        # Assert that add_misurazione method of lista_misurazioni is called with correct arguments
        mock_lista_misurazioni.add_misurazione.assert_called_once_with(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

    def test_get_lista_misurazioni(self):
        # Test that get_lista_misurazioni returns lista_misurazioni instance
        self.assertIsInstance(self.health_processor.get_lista_misurazioni(), lista_misurazioni)

    def test_clear_list(self):
        # Mocking the lista_misurazioni instance
        mock_lista_misurazioni = MagicMock()
        self.health_processor._health_processor_buffer__lista_misurazioni = mock_lista_misurazioni

        # Call method under test
        self.health_processor.clear_list()

        # Assert that clear_list method of lista_misurazioni is called
        mock_lista_misurazioni.clear_list.assert_called_once()

if __name__ == '__main__':
    unittest.main()