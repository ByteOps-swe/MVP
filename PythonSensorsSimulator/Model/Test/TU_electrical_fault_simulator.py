# pylint: skip-file
import unittest
from ..Simulators.electrical_fault_simulator import electrical_fault_simulator
from ..Simulators.coordinate import coordinate
from ..Simulators.misurazione import misurazione


class TU_electrical_fault_simulator(unittest.TestCase):
    def setUp(self):
        electrical_fault_simulator._electrical_fault_simulator__count = 0
        self.simulator = electrical_fault_simulator(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._simulator__ID_sensor, 'GstE1')
        self.assertEqual(self.simulator._simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._simulator__coordinate, coordinate)
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
        measure = self.simulator.simulate()
        self.assertIsInstance(measure, misurazione)
        self.assertIn(measure.get_value(), [0, 1])


if __name__ == '__main__':
    unittest.main()
