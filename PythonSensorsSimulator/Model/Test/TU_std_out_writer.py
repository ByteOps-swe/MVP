import unittest
from unittest.mock import Mock, patch

from ..Writers.writable import writable
from ..Writers.std_out_writer import std_out_writer

class TU_std_out_writer(unittest.TestCase):
    def setUp(self):
        self.std_out_writer = std_out_writer()
        self.mock_writable = Mock(spec=writable)

    @patch('builtins.print')
    def test_write(self, mock_print):
        self.mock_writable.to_json.return_value = '{"message": "test"}'
        self.std_out_writer.write(self.mock_writable)
        mock_print.assert_any_call('{"message": "test"}')
        mock_print.assert_any_call('Total messages printed: 1')

if __name__ == '__main__':
    unittest.main()
