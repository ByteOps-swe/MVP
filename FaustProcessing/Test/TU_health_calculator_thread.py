import unittest
from unittest.mock import Mock
from ..HealthStateModel.health_algorithm import health_algorithm
from ..HealthStateModel.Writers.writer import writer
from ..HealthStateModel.health_calculator_thread import health_calculator_thread


class TU_health_calculator_thread(unittest.TestCase):
    def setUp(self):
        self.health_calculator = Mock(spec=health_algorithm)
        self.writers = Mock(spec=writer)
        self.healthThread = health_calculator_thread(self.health_calculator, self.writers)

    def test_stop(self):
        self.healthThread.stop()
        self.assertFalse(self.healthThread._health_calculator_thread__is_running)


if __name__ == '__main__':
    unittest.main()
