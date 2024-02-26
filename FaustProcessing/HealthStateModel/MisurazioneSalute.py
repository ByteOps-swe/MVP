class MisurazioneSalute:
    def __init__(self, timestamp, value, type_, cella):
        self.__timestamp = timestamp
        self.__value = value
        self.__type = type_
        self.__cella = cella


    def to_json(self):
        return {
            "timestamp": str(self.__timestamp),
            "value": self.__value,
            "type": self.__type,
            "cella": self.__cella
        }