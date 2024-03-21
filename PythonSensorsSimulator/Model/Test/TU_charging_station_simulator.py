# pylint: skip-file
import unittest
from ..Simulators.charging_station_simulator import charging_station_simulator
from ..Simulators.coordinate import coordinate
from ..Simulators.misurazione import misurazione


class test_charging_station_simulator(unittest.TestCase):
    def setUp(self):
        charging_station_simulator._charging_station_simulator__count = 0
        self.simulator = charging_station_simulator(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._simulator__ID_sensor, 'ChS1')
        self.assertEqual(self.simulator._simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._simulator__coordinate, coordinate)
        self.assertEqual(self.simulator._misurazione, 0)

    def test_generate_measure(self):
        self.simulator._generate_measure()
        self.assertIn(self.simulator._misurazione, [True, False])

    def test_simulate(self):
        measure = self.simulator.simulate()
        self.assertIsInstance(measure, misurazione)
        self.assertIn(measure.get_value(), [True, False])


if __name__ == '__main__':
    unittest.main()
