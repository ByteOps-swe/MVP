import unittest
from unittest.mock import Mock
from ..HealthStateModel.Writers.writer import writer
from ..HealthStateModel.Writers.composite_writer import composite_writer

class TU_composite_writer(unittest.TestCase):

    def setUp(self):
        self.composite_writer = composite_writer()
        self.mock_writer = Mock(spec=writer)

    def test_add_writer(self):
        self.composite_writer.add_writer(self.mock_writer)
        self.assertEqual(len(self.composite_writer._writers), 1)
        self.assertEqual(self.composite_writer._writers[0], self.mock_writer)

    def test_remove_writer(self):
        self.composite_writer.add_writer(self.mock_writer)
        self.composite_writer.remove_writer(self.mock_writer)
        self.assertEqual(len(self.composite_writer._writers), 0)

    def test_write(self):
        self.composite_writer.add_writer(self.mock_writer)
        self.composite_writer.write('test')
        self.mock_writer.write.assert_called_once_with('test')


if __name__ == '__main__':
    unittest.main()
