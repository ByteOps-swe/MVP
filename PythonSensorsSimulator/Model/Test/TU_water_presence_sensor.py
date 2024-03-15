# pylint: skip-file
import unittest
from ..Simulators.water_presence_sensor import water_presence_sensor
from ..Simulators.coordinate import coordinate
from ..Simulators.misurazione import misurazione


class TU_water_presence_sensor(unittest.TestCase):
    def set_up(self):
        water_presence_sensor._water_presence_sensor__count = 0
        self.simulator = water_presence_sensor(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._Simulator__ID_sensor, 'Wp1')
        self.assertEqual(self.simulator._Simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._Simulator__coordinate, coordinate)
        self.assertEqual(self.simulator._misurazione, 0)

    def test_generate_measure(self):
        self.simulator._generate_measure()
        self.assertIn(self.simulator._misurazione, [True, False])

    def test_simulate(self):
        misurazione = self.simulator.simulate()
        self.assertIsInstance(misurazione, misurazione)
        self.assertIn(misurazione.get_value(), [True, False])


if __name__ == '__main__':
    unittest.main()
