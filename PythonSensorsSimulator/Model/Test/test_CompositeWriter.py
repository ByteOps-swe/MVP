import unittest
from unittest.mock import Mock, patch
from ..Writers.Writer import Writer
from ..Writers.CompositeWriter import CompositeWriter


class TestCompositeWriter(unittest.TestCase):

    def setUp(self):
        self.composite_writer = CompositeWriter()
        self.mock_writer = Mock(spec=Writer)

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
