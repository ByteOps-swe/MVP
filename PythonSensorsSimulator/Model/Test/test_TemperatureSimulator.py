# pylint: skip-file
import unittest
from ..Simulators.TemperatureSimulator import TemperatureSimulator
from ..Simulators.Coordinate import Coordinate
from ..Simulators.Misurazione import Misurazione


class TestTemperatureSimulator(unittest.TestCase):
    def setUp(self):
        TemperatureSimulator._TemperatureSimulator__count = 0
        self.simulator = TemperatureSimulator(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._Simulator__ID_sensor, 'Tmp1')
        self.assertEqual(self.simulator._Simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._Simulator__coordinate, Coordinate)
        self.assertEqual(self.simulator._misurazione, 20)

    def test_generate_measure(self):
        old_measure = self.simulator._misurazione
        self.simulator._generate_measure()
        self.assertTrue(0 <= self.simulator._misurazione <= 100)
        self.assertTrue(old_measure - 0.5 <= self.simulator._misurazione <= old_measure + 0.5)

    def test_simulate(self):
        misurazione = self.simulator.simulate()
        self.assertIsInstance(misurazione, Misurazione)
        self.assertTrue(0 <= misurazione.get_value() <= 100)


if __name__ == '__main__':
    unittest.main()
