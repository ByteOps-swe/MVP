from threading import Lock
from .Writer import Writer
from .Writable import Writable


class ListWriter(Writer):
    """
    A class that represents a writer that stores data in a list.

    Attributes:
        __data_list (list): The list to store the data.
        __lock (Lock): A lock to ensure thread-safe access to the list.
    """

    def __init__(self):
        self.__data_list = []
        self.__lock = Lock()  # Lock per garantire l'accesso thread-safe alla lista

    def write(self, to_write: Writable) -> None:
        """
        Writes the given data to the list.

        Args:
            to_write (Writable): The data to write.

        Returns:
            None
        """
        with self.__lock:
            self.__data_list.append(to_write)

    def get_data_list(self) -> list:
        """
        Returns the list of data.

        Returns:
            list: The list of data.
        """
        with self.__lock:
            return self.__data_list
