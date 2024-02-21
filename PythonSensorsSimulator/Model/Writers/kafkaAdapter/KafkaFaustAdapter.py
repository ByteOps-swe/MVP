from .KafkaTarget import KafkaTarget
import faust
import asyncio

class KafkaFaustAdapter(KafkaTarget):
    def __init__(self, topic: str, ip: str = "localhost", port: str = "9092"):
        self.app = faust.App('kafka_faust_adapter')
        self.topic = topic
        self.producer = self.app.topic(self.topic, key_type=str, value_type=str)

    async def write_to_kafka(self, data: str) -> None:
        async with self.producer.as_sync_producer() as producer:
            try:
                await producer.send(value=data)
            except Exception as e:
                print(f"Errore durante l'invio del messaggio: {e}")