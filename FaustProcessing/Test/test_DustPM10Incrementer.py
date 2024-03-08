# pylint: skip-file
import unittest
import math
from unittest.mock import Mock
from ..HealthStateModel.Incrementers.DustPM10Incrementer import DustPM10Incrementer


class TestDustPM10Incrementer(unittest.TestCase):
    def test_get_incrementation_no_measurements(self):
        # Arrange
        incrementer = DustPM10Incrementer()
        misurazioni = []

        # Act
        result = incrementer.get_incrementation(misurazioni)

        # Assert
        self.assertEqual(result, 0)

    def test_get_incrementation_single_measurement(self):
        incrementer = DustPM10Incrementer()
        misurazione = Mock()
        misurazione.get_type.return_value = "dust_level_PM10"
        misurazione.get_value.return_value = 10.0
        misurazioni = [misurazione]

        result = incrementer.get_incrementation(misurazioni)

        expected_result = int(math.log(10) * 0.1)
        self.assertEqual(result, expected_result)

    def test_get_incrementation_multiple_measurements(self):
        incrementer = DustPM10Incrementer()
        misurazione1 = Mock()
        misurazione1.get_type.return_value = "dust_level_PM10"
        misurazione1.get_value.return_value = 10.0
        misurazione2 = Mock()
        misurazione2.get_type.return_value = "dust_level_PM10"
        misurazione2.get_value.return_value = 20.0
        misurazioni = [misurazione1, misurazione2]

        result = incrementer.get_incrementation(misurazioni)

        expected_result = int((math.log(10) + math.log(20)) * 0.1)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
