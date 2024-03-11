import unittest
from unittest.mock import Mock, patch

from ..Writers.Writable import Writable
from ..Writers.StdoutWriter import StdoutWriter

class TestStdoutWriter(unittest.TestCase):
    def setUp(self):
        self.stdout_writer = StdoutWriter()
        self.mock_writable = Mock(spec=Writable)

    @patch('builtins.print')
    def test_write(self, mock_print):
        self.mock_writable.to_json.return_value = '{"message": "test"}'
        self.stdout_writer.write(self.mock_writable)
        mock_print.assert_any_call('{"message": "test"}')
        mock_print.assert_any_call('Total messages printed: 1')

if __name__ == '__main__':
    unittest.main()
