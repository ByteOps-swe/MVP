import unittest
from unittest.mock import Mock
from ..HealthStateModel.HealthAlgorithm import HealthAlgorithm
from ..HealthStateModel.Writers.Writer import Writer
from ..HealthStateModel.HealthCalculatorThread import HealthCalculatorThread


class TestHealthCalculatorThread(unittest.TestCase):
    def setUp(self):
        self.healthCalculator = Mock(spec=HealthAlgorithm)
        self.writers = Mock(spec=Writer)
        self.healthThread = HealthCalculatorThread(self.healthCalculator, self.writers)

    def test_stop(self):
        self.healthThread.stop()
        self.assertFalse(self.healthThread._HealthCalculatorThread__is_running)


if __name__ == '__main__':
    unittest.main()
