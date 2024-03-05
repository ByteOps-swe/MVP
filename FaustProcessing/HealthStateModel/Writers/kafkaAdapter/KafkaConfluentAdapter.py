from .KafkaTarget import KafkaTarget
from confluent_kafka import Producer, KafkaException

#Adattatore per la l'invio tramite libreria confluent kafka
def acked(err, msg):
    """
    Callback function for message acknowledgment.

    Args:
        err (str): The error message, if any.
        msg (str): The message that was acknowledged.

    Returns:
        None
    """
    if err is not None:
        print("Fallimento nella consegna del messaggio: %s: %s" %
              (str(msg), str(err)))

class KafkaConfluentAdapter(KafkaTarget):
    """
    A class representing a Kafka adapter using the Confluent Kafka library.

    Args:
        topic (str): The topic to which the data will be written.
        ip (str, optional): The IP address of the Kafka broker. Defaults to "kafka".
        port (str, optional): The port number of the Kafka broker. Defaults to "9092".
    """

    def __init__(self, topic: str, ip: str = "kafka", port: int = 9092):
        self.__topic = topic
        config = {'bootstrap.servers': ip + ':' + str(port)}
        try:
            self.__producer = Producer(config)
        except KafkaException as e:
            print(f"Errore nella creazione del producer: {e}")

    def write_to_kafka(self, data: str) -> None:
        """
        Writes the given data to the Kafka topic.

        Args:
            data (str): The data to be written to Kafka.
        """
        try:
            self.__producer.produce(self.__topic, value=data, callback=acked)
            self.__producer.poll(1)
        except KafkaException as e:
            print(f"Errore durante la scrittura in Kafka: {e}")
