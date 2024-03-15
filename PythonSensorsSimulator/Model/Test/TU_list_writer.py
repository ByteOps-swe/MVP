import unittest
from unittest.mock import Mock
from ..Writers import writable
from ..Writers.list_writer import list_writer


class TU_list_writer(unittest.TestCase):

    def set_up(self):
        self.list_writer = list_writer()
        self.mock_writable = Mock(spec=writable)

    def test_write(self):
        self.list_writer.write(self.mock_writable)
        data_list = self.list_writer.get_data_list()
        self.assertEqual(len(data_list), 1)
        self.assertEqual(data_list[0], self.mock_writable)

    def test_thread_safety(self):
        self.list_writer.write(self.mock_writable)
        self.list_writer.write(self.mock_writable)
        data_list = self.list_writer.get_data_list()
        self.assertEqual(len(data_list), 2)


if __name__ == '__main__':
    unittest.main()
