import unittest
from ..HealthStateModel.Coordinate import Coordinate  # Replace 'your_module' with the actual module name


class TestCoordinate(unittest.TestCase):
    def setUp(self):
        # Initialize a Coordinate instance for testing
        self.coordinates = Coordinate(latitude=40.7128, longitude=-74.0060)

    def test_get_latitude(self):
        self.assertEqual(self.coordinates.get_latitude(), 40.7128)

    def test_get_longitude(self):
        self.assertEqual(self.coordinates.get_longitude(), -74.0060)


if __name__ == "__main__":
    unittest.main()
