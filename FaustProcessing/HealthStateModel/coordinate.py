class coordinate():
    def __init__(self, latitude:float, longitude: float):
        self.__latitude = latitude
        self.__longitude = longitude

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude
