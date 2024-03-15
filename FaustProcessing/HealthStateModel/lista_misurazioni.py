from typing import List
from .misurazione import misurazione
from .coordinate import coordinate

class lista_misurazioni:
    def __init__(self):
        self.__list: List[misurazione] = []

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        self.__list.append(misurazione(timestamp, value, type_, coordinate(latitude, longitude), ID_sensore, cella))

    def clear_list(self):
        self.__list.clear()

    def get_list_by_cella_and_type(self, cella: str, tipo_dato: str):
        return [misurazione for misurazione in self.__list if misurazione.get_cella() == cella and misurazione.get_type() == tipo_dato]

    def get_unique_celle(self):
        unique_celle = set()
        for misurazione in self.__list:
            unique_celle.add(misurazione.get_cella())
        return list(unique_celle)
