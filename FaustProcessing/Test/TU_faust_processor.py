import unittest
from unittest.mock import Mock
from ..ProcessingAdapter.faust_processor import processor, faust_measurement
import asyncio

class TestProcessor(unittest.TestCase):

    def test_process_abstract_method(self):
        # Create a mock subclass implementing the abstract method
        class MockProcessor(processor):
            async def process(self, misurazione: faust_measurement):
                pass

        # Instantiate the mock subclass
        mock_processor = MockProcessor()

        # Mock a faust_measurement object
        mock_misurazione = Mock(spec=faust_measurement)

        # Call the process method
        asyncio.run(mock_processor.process(mock_misurazione))

        # Ensure that the abstract method has been properly overridden
        self.assertTrue(hasattr(MockProcessor, 'process'))
        self.assertTrue(callable(MockProcessor.process))
        self.assertTrue('abstractmethod' not in MockProcessor.process.__dict__)

if __name__ == '__main__':
    unittest.main()