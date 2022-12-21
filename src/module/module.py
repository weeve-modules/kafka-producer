"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from kafka import KafkaProducer
from json import dumps
from os import getenv

log = getLogger("module")

__TOPIC__ = getenv("TOPIC")
__PARTITION__ = int(getenv("PARTITION")) if getenv("PARTITION") else None
__FLUSH_BUFFER__ = bool(getenv("FLUSH_BUFFER"))

producer = KafkaProducer(
    bootstrap_servers=[server.strip() for server in getenv("BOOTSTRAP_SERVERS", "").split(',')],
    client_id=getenv("CLIENT_ID", ""),
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

def on_success(record):
    log.debug(f'Success! Topic: {record.topic}. Partition: {record.partition}. Offset: {record.offset}.')

def on_error(excp):
    log.error(f'Error when sending to Kafka (producer.send()): {excp}')
    raise Exception(f'Error when sending to Kafka (producer.send()): {excp}')


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        producer.send(
            topic=__TOPIC__,
            value=received_data,
            partition=__PARTITION__,
        ).add_callback(on_success).add_errback(on_error)

        if __FLUSH_BUFFER__:
            # block until all async messages are sent -> eventually, the producer is also flushed (producer.flush()),
            # that means blocking it until previous messaged have been delivered effectively, to make it synchronous.
            producer.flush()

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
