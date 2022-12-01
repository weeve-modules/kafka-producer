# Kafka Producer

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Kafka Producer                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/kafka-producer](https://hub.docker.com/r/weevenetwork/kafka-producer) |
| Authors        | Jakub Grzelak                    |

- [Kafka Producer](#kafka-producer)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Producer to connect with Apache Kafka and publish data to the cluster. The module uses `utf-8` encoding for value serializer.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Topic    | TOPIC         | string   | Kafka topic to publish to.            |
| Bootstrap Servers    | BOOTSTRAP_SERVERS         | string   | List of comma (,) separated Kafka bootstrap servers that the producer should contact to bootstrap initial cluster metadata.            |
| Client ID    | CLIENT_ID         | string   | A name for this client. This string is passed in each request to servers and can be used to identify specific server-side log entries that correspond to this client.            |
| Partition    | PARTITION         | string   | Optionally specify a partition. If not set the message is delivered to a random partition (filtered to partitions with available leaders only, if possible).            |
| Flush Buffer    | FLUSH_BUFFER         | string   | Make producer flushed blocking it until previous messaged have been delivered effectively, to make it synchronous.            |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
kafka-python
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

## Output

Output of this module is:

Input json object published to the selected Kafka cluster and topic.
