class Misurazione:
    def __init__(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        self.timestamp = timestamp
        self.value = value
        self.type = type_
        self.latitude = latitude
        self.longitude = longitude
        self.ID_sensore = ID_sensore
        self.cella = cella

    @classmethod
    def from_json(cls, json_data):
        timestamp = json_data["timestamp"]
        value = json_data["value"]
        type_ = json_data["type"]
        latitude = json_data["latitude"]
        longitude = json_data["longitude"]
        ID_sensore = json_data["ID_sensore"]
        cella = json_data["cella"]
        return cls(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

    def to_json(self):
        return {
            "timestamp": str(self.timestamp),
            "value": self.__format_value(self.value),
            "type": self.type,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "ID_sensore": self.ID_sensore,
            "cella": self.cella
        }

    def __format_value(self, value):
        if isinstance(value, bool):
            return 1 if value else 0
        elif isinstance(value, float):
            return "{:.2f}".format(value)
        else:
            return value
