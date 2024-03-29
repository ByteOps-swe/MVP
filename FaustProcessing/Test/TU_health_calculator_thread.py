import unittest
from unittest.mock import Mock
from ..HealthStateModel.health_algorithm import health_algorithm
from ..HealthStateModel.Writers.writer import writer
from ..HealthStateModel.health_calculator_thread import health_calculator_thread, adapter_misurazione
import time

class TU_health_calculator_thread(unittest.TestCase):
    def setUp(self):
        self.health_calculator = Mock(spec=health_algorithm)
        self.writers = Mock(spec=writer)
        self.healthThread = health_calculator_thread(self.health_calculator, self.writers)

    def test_run(self):
        # Set up mock behavior
        self.health_calculator.generate_new_health_score.return_value = [{'timestamp': '2024-03-28 10:00:00', 'value': 75}]
        self.writers.write.return_value = None

        # Run the thread
        self.healthThread.start()

        # Let it run for a short period of time
        time.sleep(0.1)

        # Stop the thread
        self.healthThread.stop()

        # Assert mock method calls
        self.health_calculator.generate_new_health_score.assert_called()

    def test_stop(self):
        self.healthThread.stop()
        self.assertFalse(self.healthThread._health_calculator_thread__is_running)


if __name__ == '__main__':
    unittest.main()