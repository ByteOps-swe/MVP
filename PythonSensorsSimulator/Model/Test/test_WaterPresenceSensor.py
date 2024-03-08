# pylint: skip-file
import unittest
from ..Simulators.WaterPresenceSensor import WaterPresenceSensor
from ..Simulators.Coordinate import Coordinate
from ..Simulators.Misurazione import Misurazione


class TestWaterPresenceSensor(unittest.TestCase):
    def setUp(self):
        WaterPresenceSensor._WaterPresenceSensor__count = 0
        self.simulator = WaterPresenceSensor(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._Simulator__ID_sensor, 'Wp1')
        self.assertEqual(self.simulator._Simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._Simulator__coordinate, Coordinate)
        self.assertEqual(self.simulator._misurazione, 0)

    def test_generate_measure(self):
        self.simulator._generate_measure()
        self.assertIn(self.simulator._misurazione, [True, False])

    def test_simulate(self):
        misurazione = self.simulator.simulate()
        self.assertIsInstance(misurazione, Misurazione)
        self.assertIn(misurazione.get_value(), [True, False])


if __name__ == '__main__':
    unittest.main()
