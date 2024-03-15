# pylint: skip-file
import unittest
from unittest.mock import Mock
from ..HealthStateModel.Incrementers.humidity_incrementer import humidity_incrementer

class TU_humidity_incrementer(unittest.TestCase):
    def test_get_incrementation_no_measurements(self):
        # Arrange
        incrementer = humidity_incrementer()
        misurazioni = []

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 0)

    def test_get_incrementation_within_threshold(self):
        # Arrange
        incrementer = humidity_incrementer()
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
        incrementer = humidity_incrementer()
        misurazione = Mock()
        misurazione.get_type.return_value = "humidity"
        misurazione.get_value.return_value = 80.0
        misurazioni = [misurazione]

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 10)

    def test_get_incrementation_below_threshold(self):
        # Arrange
        incrementer = humidity_incrementer()
        misurazione = Mock()
        misurazione.get_type.return_value = "humidity"
        misurazione.get_value.return_value = 20.0
        misurazioni = [misurazione]

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 10) 

if __name__ == "__main__":
    unittest.main()
