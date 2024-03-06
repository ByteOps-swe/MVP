import unittest
from ..Simulators.EcologicalIslandSimulator import EcologicalIslandSimulator
from ..Simulators.Coordinate import Coordinate
from ..Simulators.Misurazione import Misurazione


class TestEcologicalIslandSimulator(unittest.TestCase):
    def setUp(self):
        EcologicalIslandSimulator._EcologicalIslandSimulator__count = 0
        self.simulator = EcologicalIslandSimulator(45.0, 10.0, 'cella1')

    def test_init(self):
        self.assertEqual(self.simulator._Simulator__ID_sensor, 'EcoIsl1')
        self.assertEqual(self.simulator._Simulator__cella_sensore, 'cella1')
        self.assertIsInstance(self.simulator._Simulator__coordinate, Coordinate)
        self.assertEqual(self.simulator._misurazione, 50)

    def test_generate_measure(self):
        old_measure = self.simulator._misurazione
        self.simulator._generate_measure()
        self.assertTrue(
            EcologicalIslandSimulator._EcologicalIslandSimulator__min_fill_percentage <=
            self.simulator._misurazione <=
            EcologicalIslandSimulator._EcologicalIslandSimulator__max_fill_percentage)
        self.assertTrue(
            old_measure - EcologicalIslandSimulator._EcologicalIslandSimulator__fill_rate <=
            self.simulator._misurazione <=
            old_measure + EcologicalIslandSimulator._EcologicalIslandSimulator__fill_rate)

    def test_simulate(self):
        misurazione = self.simulator.simulate()
        self.assertIsInstance(misurazione, Misurazione)
        self.assertTrue(
            EcologicalIslandSimulator._EcologicalIslandSimulator__min_fill_percentage
              <= misurazione.get_value() <= 
              EcologicalIslandSimulator._EcologicalIslandSimulator__max_fill_percentage)


if __name__ == '__main__':
    unittest.main()
