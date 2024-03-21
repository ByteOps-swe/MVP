# pylint: skip-file
import unittest
from unittest.mock import Mock
from ..HealthStateModel.Incrementers.temperature_incrementer import temperature_incrementer

class TU_temperature_incrementer(unittest.TestCase):
    def setUp(self):
        self.temp_incrementer = temperature_incrementer(20, 30, "temperature")

    def test_get_incrementation(self):
        misurazione1 = Mock()
        misurazione1.get_type.return_value = "temperature"
        misurazione1.get_value.return_value = "35"

        misurazione2 = Mock()
        misurazione2.get_type.return_value = "temperature"
        misurazione2.get_value.return_value = "35"

        misurazione3 = Mock()
        misurazione3.get_type.return_value = "temperature"
        misurazione3.get_value.return_value = "15"

        misurazioni = [misurazione1, misurazione2, misurazione3]
        self.assertEqual(self.temp_incrementer.get_incrementation(misurazioni), 15)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
