from .Incrementer import Incrementer

class HumidityIncrementer(Incrementer):
    def __init__(self, upper_health_soglia=70, under_health_soglia=30):
        self.__upper_health_soglia = upper_health_soglia
        self.__under_health_soglia = under_health_soglia
    
    def get_incrementation(self, dato): #da definire
        if self.__under_health_soglia <= dato <= self.__upper_health_soglia:
            return 0
        elif dato > self.__upper_health_soglia:
            return dato - self.__upper_health_soglia
        else:
            return self.__under_health_soglia - dato
