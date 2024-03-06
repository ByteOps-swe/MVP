from confluent_kafka import Producer, KafkaException
from .KafkaTarget import KafkaTarget

#Adattatore per la l'invio tramite libreria confluent kafka
def acked(err, msg):
    """
    Callback function for message acknowledgment.

    Parameters:
    - err (Exception or None): The error that occurred during message delivery, if any.
    - msg (Message): The message that was delivered.

    Returns:
    None
    """
    if err is not None:
        print(f"Fallimento nella consegna del messaggio: {msg}: {err}")

class KafkaConfluentAdapter(KafkaTarget):
    """
    A class representing a Kafka adapter using the Confluent Kafka library.

    Args:
        topic (str): The Kafka topic to write data to.
        ip (str, optional): The IP address of the Kafka broker. Defaults to "kafka".
        port (str, optional): The port number of the Kafka broker. Defaults to "9092".
    """

    def __init__(self, topic: str, ip: str = "kafka", port: str = "9092"):
        self.__topic = topic
        config = {'bootstrap.servers': ip + ':' + port}
        try:
            self.__producer = Producer(config)
        except KafkaException as e:
            print(f"Errore nella creazione del producer: {e}")

    def write_to_kafka(self, data: str) -> None:
        """
        Writes data to the Kafka topic.

        Args:
            data (str): The data to be written to Kafka.
        """
        try:
            self.__producer.produce(self.__topic, value=data, callback=acked)
            self.__producer.poll(1)
        except KafkaException as e:
            print(f"Errore durante la scrittura in Kafka: {e}")

    def flush_kafka_producer(self):
        """
        Flushes the Kafka producer to ensure all messages are sent.

        Raises:
            Exception: If an error occurs while flushing the Kafka producer.
        """
        try:
            self.__producer.flush()
        except Exception as e:
            print(f"Error while flushing Kafka producer: {e}")
