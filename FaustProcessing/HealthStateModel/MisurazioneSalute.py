class MisurazioneSalute():
    def __init__(self, timestamp, value, type_, cella):
        self.__timestamp = timestamp
        self.__value = value
        self.__type = type_
        self.__cella = cella

    def get_timestamp(self):
        return self.__timestamp
    
    def get_value(self):
        return self.__value
    
    def get_type(self):
        return self.__type
    
    def get_cella(self):
        return self.__cella
    