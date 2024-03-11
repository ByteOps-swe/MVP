import unittest
from unittest.mock import Mock
from ..Writers.Writable import Writable
from ..Writers.ListWriter import ListWriter


class TestListWriter(unittest.TestCase):

    def setUp(self):
        self.list_writer = ListWriter()
        self.mock_writable = Mock(spec=Writable)

    def test_write(self):
        self.list_writer.write(self.mock_writable)
        data_list = self.list_writer.get_data_list()
        self.assertEqual(len(data_list), 1)
        self.assertEqual(data_list[0], self.mock_writable)

    def test_thread_safety(self):
        # Questo è un test molto semplice e potrebbe non coprire tutti i casi di concorrenza.
        # Potrebbe essere necessario un test più robusto per garantire la sicurezza del thread.
        self.list_writer.write(self.mock_writable)
        self.list_writer.write(self.mock_writable)
        data_list = self.list_writer.get_data_list()
        self.assertEqual(len(data_list), 2)


if __name__ == '__main__':
    unittest.main()
