import faust
class faust_measurement(faust.Record, serializer='json'):
    timestamp: str
    value: float
    type: str
    latitude: float
    longitude: float
    ID_sensore: str
    cella: str
