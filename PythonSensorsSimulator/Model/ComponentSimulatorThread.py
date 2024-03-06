import threading
from abc import  abstractmethod

class ComponentSimulatorThread(threading.Thread):
    """
    A base class for creating component simulator threads.

    This class provides an abstract implementation of a thread that simulates a component.
    Subclasses must implement the `run` and `stop` methods.

    Attributes:
        None

    Methods:
        run: The main method that will be executed when the thread starts.
        stop: Stops the execution of the thread.

    """

    @abstractmethod
    def run(self) -> None:
        """
        Executes the logic of the thread.

        This method is called when the thread is started. It contains the main logic
        that will be executed in a separate thread.

        Parameters:
            None

        Returns:
            None
        """
    @abstractmethod
    def task(self) -> None:
        """
        Parameters:
            None

        Returns:
            None
        """
    @abstractmethod
    def stop(self) -> None:
        """
        Stops the component simulator thread.
        """
