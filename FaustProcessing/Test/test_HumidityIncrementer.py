# pylint: skip-file
import unittest
from unittest.mock import Mock
from ..HealthStateModel.Incrementers.HumidityIncrementer import HumidityIncrementer

class TestHumidityIncrementer(unittest.TestCase):
    def test_get_incrementation_no_measurements(self):
        # Arrange
        incrementer = HumidityIncrementer()
        misurazioni = []

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 0)

    def test_get_incrementation_within_threshold(self):
        # Arrange
        incrementer = HumidityIncrementer()
        misurazione = Mock()
        misurazione.get_type.return_value = "humidity"
        misurazione.get_value.return_value = 50.0
        misurazioni = [misurazione]

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 0)

    def test_get_incrementation_above_threshold(self):
        # Arrange
        incrementer = HumidityIncrementer()
        misurazione = Mock()
        misurazione.get_type.return_value = "humidity"
        misurazione.get_value.return_value = 80.0
        misurazioni = [misurazione]

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 10)  # Assuming upper threshold is 70

    def test_get_incrementation_below_threshold(self):
        # Arrange
        incrementer = HumidityIncrementer()
        misurazione = Mock()
        misurazione.get_type.return_value = "humidity"
        misurazione.get_value.return_value = 20.0
        misurazioni = [misurazione]

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 10)  # Assuming lower threshold is 30

if __name__ == "__main__":
    unittest.main()
