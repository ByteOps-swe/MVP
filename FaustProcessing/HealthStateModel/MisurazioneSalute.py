class MisurazioneSalute:
    def __init__(self, timestamp, value, type_, cella):
        self.timestamp = timestamp
        self.value = value
        self.type = type_
        self.cella = cella


    def to_json(self):
        return {
            "timestamp": str(self.timestamp),
            "value": self.value,
            "type": self.type,
            "cella": self.cella
        }