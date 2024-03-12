import unittest
from unittest.mock import Mock
from ..HealthStateModel.AdapterMisurazioneSalute import AdapterMisurazione


class TestAdapterMisurazione(unittest.TestCase):
    def setUp(self):
        self.misurazione = Mock()  # Crea un oggetto mock
        self.adapter = AdapterMisurazione(self.misurazione)

    def test_to_json(self):
        self.misurazione.get_timestamp.return_value = '2024-03-12 11:03:46'
        self.misurazione.get_value.return_value = 100
        self.misurazione.get_type.return_value = 'tipo'
        self.misurazione.get_cella.return_value = 'cella'

        expected_output = {
            "timestamp": '2024-03-12 11:03:46',
            "value": 100,
            "type": 'tipo',
            "cella": 'cella'
        }
        self.assertEqual(self.adapter.to_json(), expected_output)


if __name__ == '__main__':
    unittest.main()
