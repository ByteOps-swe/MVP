# pylint: skip-file
import unittest
from ..HealthStateModel.health_calculator import health_calculator

class TU_health_calculator(unittest.TestCase):

    def setUp(self):
        self.calculator = health_calculator()

    def test_add_misurazione(self):
        self.calculator.add_misurazione("2024-03-07 09:07:00", 25, "temperature", 45.4642, 9.1900, "ID1", "cella1")
        initial_health_scores = self.calculator.generate_new_health_score()

        self.calculator.add_misurazione("2024-03-07 09:08:00", 26, "temperature", 45.4642, 9.1900, "ID1", "cella1")
        new_health_scores = self.calculator.generate_new_health_score()

        self.assertNotEqual(initial_health_scores, new_health_scores)

    def test_generate_new_health_score(self):
        self.calculator.add_misurazione("2024-03-07 09:07:00", 25, "temperature", 45.4642, 9.1900, "ID1", "cella1")
        self.calculator.add_misurazione("2024-03-07 09:07:00", 60, "humidity", 45.4642, 9.1900, "ID1", "cella1")
        self.calculator.add_misurazione("2024-03-07 09:07:00", 50, "dust_PM10", 45.4642, 9.1900, "ID1", "cella1")
        health_scores = self.calculator.generate_new_health_score()
        self.assertEqual(len(health_scores), 1)


if __name__ == '__main__':
    unittest.main()
