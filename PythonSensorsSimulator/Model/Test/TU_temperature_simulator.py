# pylint: skip-file
import unittest
from ..Simulators.temperature_simulator import temperature_simulator
from ..Simulators.coordinate import coordinate
from ..Simulators.misurazione import misurazione


class TU_temperature_simulator(unittest.TestCase):
    def set_up(self):
        temperature_simulator._temperature_simulator__count = 0
        self.simulator = temperature_simulator(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._Simulator__ID_sensor, 'Tmp1')
        self.assertEqual(self.simulator._Simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._Simulator__coordinate, coordinate)
        self.assertEqual(self.simulator._misurazione, 20)

    def test_generate_measure(self):
        old_measure = self.simulator._misurazione
        self.simulator._generate_measure()
        self.assertTrue(0 <= self.simulator._misurazione <= 100)
        self.assertTrue(old_measure - 0.5 <= self.simulator._misurazione <= old_measure + 0.5)

    def test_simulate(self):
        misurazione = self.simulator.simulate()
        self.assertIsInstance(misurazione, misurazione)
        self.assertTrue(0 <= misurazione.get_value() <= 100)


if __name__ == '__main__':
    unittest.main()
