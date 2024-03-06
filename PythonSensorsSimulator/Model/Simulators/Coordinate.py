class Coordinate():
    def __init__(self, latitude:float, longitude: float):
        self.__latitude = latitude
        self.__longitude = longitude

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return (self.__latitude == other.get_latitude() and
                self.__longitude == other.get_longitude())
    