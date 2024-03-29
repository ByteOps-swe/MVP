import unittest
from unittest.mock import Mock
from ..ProcessingAdapter.health_model_processor_adapter import health_model_processor_adapter, health_processor_buffer, faust_measurement

import asyncio

class TestHealthModelProcessorAdapter(unittest.TestCase):

    def test_process(self):
        # Mocking dependencies
        mock_health_calculator = Mock(spec=health_processor_buffer)
        mock_misurazione = Mock(spec=faust_measurement)

        # Instantiate the class under test with mocked dependencies
        adapter = health_model_processor_adapter(mock_health_calculator)

        # Call the method under test
        asyncio.run(adapter.process(mock_misurazione))

        # Assert that add_misurazione method of health_calculator is called with correct arguments
        mock_health_calculator.add_misurazione.assert_called_once_with(
            mock_misurazione.timestamp,
            mock_misurazione.value,
            mock_misurazione.type,
            mock_misurazione.latitude,
            mock_misurazione.longitude,
            mock_misurazione.ID_sensore,
            mock_misurazione.cella
        )

if __name__ == '__main__':
    unittest.main()