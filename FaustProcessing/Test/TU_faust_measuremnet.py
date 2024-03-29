import unittest
from ..ProcessingAdapter.faust_measurement import faust_measurement

class TestFaustMeasurement(unittest.TestCase):

    def test_attributes(self):
        # Test data
        timestamp = "2024-03-28 10:00:00"
        value = 25.5
        type_ = "Temperature"
        latitude = 37.7749
        longitude = -122.4194
        ID_sensore = "ABC123"
        cella = "A1"

        # Create an instance of the faust_measurement class
        measurement = faust_measurement(
            timestamp=timestamp,
            value=value,
            type=type_,
            latitude=latitude,
            longitude=longitude,
            ID_sensore=ID_sensore,
            cella=cella
        )

        # Assert that attributes are set correctly
        self.assertEqual(measurement.timestamp, timestamp)
        self.assertEqual(measurement.value, value)
        self.assertEqual(measurement.type, type_)
        self.assertEqual(measurement.latitude, latitude)
        self.assertEqual(measurement.longitude, longitude)
        self.assertEqual(measurement.ID_sensore, ID_sensore)
        self.assertEqual(measurement.cella, cella)

    def test_serialization(self):
        # Test data
        timestamp = "2024-03-28 10:00:00"
        value = 25.5
        type_ = "Temperature"
        latitude = 37.7749
        longitude = -122.4194
        ID_sensore = "ABC123"
        cella = "A1"

        # Create an instance of the faust_measurement class
        measurement = faust_measurement(
            timestamp=timestamp,
            value=value,
            type=type_,
            latitude=latitude,
            longitude=longitude,
            ID_sensore=ID_sensore,
            cella=cella
        )

        # Serialize the instance
        serialized = measurement.dumps()

        # Deserialize the serialized data
        deserialized = faust_measurement.loads(serialized)

        # Assert that the deserialized instance matches the original
        self.assertEqual(measurement, deserialized)

if __name__ == '__main__':
    unittest.main()