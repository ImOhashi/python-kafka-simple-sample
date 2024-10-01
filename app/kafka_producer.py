from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging as log


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

message = producer.send('test-topic', b'any text message')

try: 
    record_metadata = message.get(timeout=10)
except KafkaError:
    log.exception()
    pass

print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)