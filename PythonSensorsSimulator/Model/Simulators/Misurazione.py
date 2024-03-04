from .Coordinate import Coordinate
import datetime
class Misurazione():
    def __init__(self, timestamp:datetime, value, type_:str, coordinate: Coordinate, ID_sensore:str, cella:str):
        self.__timestamp = timestamp
        self.__value = value
        self.__type = type_
        self.__coordinates = coordinate
        self.__ID_sensore = ID_sensore
        self.__cella = cella
        
    def get_timestamp(self):
        return self.__timestamp
    
    def get_value(self):
        return self.__value
    
    def get_type(self):
        return self.__type
    
    def get_latitude(self):
        return self.__coordinates.get_latitude()
    
    def get_longitude(self):
        return self.__coordinates.get_longitude()
    
    def get_ID_sensore(self):
        return self.__ID_sensore
    
    def get_cella(self):
        return self.__cella
   
    def __eq__(self, other):
            if not isinstance(other, Misurazione):
                return False
            
            return (
                    str(self.__timestamp) == str(other.__timestamp) and
                    self.__value == other.__value and
                    self.__type == other.__type and
                    self.__coordinates == other.__coordinates and
                    self.__ID_sensore == other.__ID_sensore and
                    self.__cella == other.__cella)