import threading
from .Writer import Writer
from .Writable import Writable

class StdoutWriter(Writer):
    """
    A class that writes data to the standard output (stdout).

    This class inherits from the Writer class and provides a method to write data to the standard output.
    It also keeps track of the number of messages printed.

    Attributes:
        __counter_lock (threading.Lock): A lock to synchronize access to the message counter.
        __message_counter (int): The total number of messages printed.

    Methods:
        __init__(): Initializes the StdoutWriter object.
        write(to_write: Writable) -> None: Writes the given data to the standard output.
        __update_counter(): Updates the message counter.

    """

    __counter_lock = threading.Lock()
    __message_counter = 0

    def __init__(self):
        """
        Initializes the StdoutWriter object.
        """
        self.__lock = threading.Lock()

    def write(self, to_write: Writable) -> None:
        """
        Writes the given data to the standard output.

        Args:
            to_write (Writable): The data to be written.

        Returns:
            None
        """
        with self.__lock:
            print(to_write.to_json())
            self.__update_counter()

    @classmethod
    def __update_counter(cls):
        """
        Updates the message counter.

        This method is called after each write operation to increment the message counter.

        Returns:
            None
        """
        with cls.__counter_lock:
            cls.__message_counter += 1
            print(f"Total messages printed: {cls.__message_counter}")
