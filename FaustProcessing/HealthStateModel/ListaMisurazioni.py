from typing import List
from .Misurazione import Misurazione
from .Coordinate import Coordinate

class ListaMisurazioni:
    """
    A class representing a list of measurements.

    Attributes:
    __list (List[Misurazione]): The list of measurements.

    Methods:
    add_misurazione: Add a new measurement to the list.
    clear_list: Clear the list of measurements.
    get_list_by_cella_and_type: Get a list of measurements filtered by cella and tipo_dato.
    get_unique_celle: Get a list of unique celle from the measurements.
    """

    def __init__(self):
        self.__list: List[Misurazione] = []

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        """
        Add a new measurement to the list.

        Args:
        timestamp: The timestamp of the measurement.
        value: The value of the measurement.
        type_: The type of the measurement.
        latitude: The latitude of the measurement.
        longitude: The longitude of the measurement.
        ID_sensore: The ID of the sensor.
        cella: The cella of the measurement.
        """
        self.__list.append(Misurazione(timestamp, value, type_, Coordinate(latitude, longitude), ID_sensore, cella))

    def clear_list(self):
        """
        Clear the list of measurements.
        """
        self.__list.clear()

    def get_list_by_cella_and_type(self, cella: str, tipo_dato: str):
        """
        Get a list of measurements filtered by cella and tipo_dato.

        Args:
        cella: The cella to filter by.
        tipo_dato: The tipo_dato to filter by.

        Returns:
        A list of measurements that match the given cella and tipo_dato.
        """
        return [misurazione for misurazione in self.__list if misurazione.get_cella() == cella and misurazione.get_type() == tipo_dato]
    def get_unique_celle(self):
        """
        Get a list of unique celle from the measurements.

        Returns:
        A list of unique celle from the measurements.
        """
        unique_celle = set()  
        for misurazione in self.__list:
            unique_celle.add(misurazione.get_cella())
        return list(unique_celle)
    