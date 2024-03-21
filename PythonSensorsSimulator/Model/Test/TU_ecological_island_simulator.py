# pylint: skip-file
import unittest
from ..Simulators.ecological_island_simulator import ecological_island_simulator
from ..Simulators.coordinate import coordinate
from ..Simulators.misurazione import misurazione


class TU_ecological_island_simulator(unittest.TestCase):
    def setUp(self):
        ecological_island_simulator._ecological_island_simulator__count = 0
        self.simulator = ecological_island_simulator(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._simulator__ID_sensor, 'EcoIsl1')
        self.assertEqual(self.simulator._simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._simulator__coordinate, coordinate)
        self.assertEqual(self.simulator._misurazione, 50)

    def test_generate_measure(self):
        old_measure = self.simulator._misurazione
        self.simulator._generate_measure()
        self.assertTrue(
            ecological_island_simulator._ecological_island_simulator__min_fill_percentage <=
            self.simulator._misurazione <=
            ecological_island_simulator._ecological_island_simulator__max_fill_percentage)
        self.assertTrue(
            old_measure - ecological_island_simulator._ecological_island_simulator__fill_rate <=
            self.simulator._misurazione <=
            old_measure + ecological_island_simulator._ecological_island_simulator__fill_rate)

    def test_simulate(self):
        measure = self.simulator.simulate()
        self.assertIsInstance(measure, misurazione)
        self.assertTrue(
            ecological_island_simulator._ecological_island_simulator__min_fill_percentage
              <= measure.get_value() <= 
              ecological_island_simulator._ecological_island_simulator__max_fill_percentage)


if __name__ == '__main__':
    unittest.main()
