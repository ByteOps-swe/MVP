import unittest
from ..HealthStateModel.coordinate import coordinate


class TU_coordinate(unittest.TestCase):
    def setUp(self):
        self.coordinates = coordinate(latitude=40.7128, longitude=-74.0060)

    def test_get_latitude(self):
        self.assertEqual(self.coordinates.get_latitude(), 40.7128)

    def test_get_longitude(self):
        self.assertEqual(self.coordinates.get_longitude(), -74.0060)


if __name__ == "__main__":
    unittest.main()
