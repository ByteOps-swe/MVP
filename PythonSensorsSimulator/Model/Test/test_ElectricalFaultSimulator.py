# pylint: skip-file
import unittest
from ..Simulators.ElectricalFaultSimulator import ElectricalFaultSimulator
from ..Simulators.Coordinate import Coordinate
from ..Simulators.Misurazione import Misurazione


class TestElectricalFaultSimulator(unittest.TestCase):
    def setUp(self):
        ElectricalFaultSimulator._ElectricalFaultSimulator__count = 0
        self.simulator = ElectricalFaultSimulator(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._Simulator__ID_sensor, 'GstE1')
        self.assertEqual(self.simulator._Simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._Simulator__coordinate, Coordinate)
        self.assertEqual(self.simulator._misurazione, 0)

    def test_generate_measure(self):
        old_measure = self.simulator._misurazione
        self.simulator._generate_measure()
        self.assertIn(self.simulator._misurazione, [0, 1])
        if old_measure == 1:
            self.assertEqual(self.simulator._fault_probability, 0.2)
        else:
            self.assertEqual(self.simulator._fault_probability, 0.1)

    def test_simulate(self):
        misurazione = self.simulator.simulate()
        self.assertIsInstance(misurazione, Misurazione)
        self.assertIn(misurazione.get_value(), [0, 1])


if __name__ == '__main__':
    unittest.main()
