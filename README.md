# scylla-perf

ScyllaDB challenge

## Introduction

This repository contains a simple example of how to deploy a ScyllaDB cluster and run a performance test using cassandra-stress.

## Table of Contents

...

## Requirements

- Docker
- ScyllaDB image
- Cassandra-stress image

## Deploying a ScyllaDB cluster

To deploy a single node ScyllaDB cluster, you can use the following command:

```bash
docker run --name some-scylla --hostname some-scylla -p 9042:9042 -d scylladb/scylla --smp 1
```

This will create a scylla container with 1 core. You can change the number of cores by changing the `--smp` parameter. The hostname is set to `some-scylla` in this case.

In our example we will expose the port 9042 to the host machine. This is the default port for CQL.

The container will be running in the background. You can check the logs by running:

```bash
docker logs some-scylla | tail
```

## Finding the host IP

To find the IP address of the host machine, you can run the following command:

```bash
export HOST_IP=$(docker exec -it some-scylla nodetool status | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b")
```

This will use the node tool to get the status of the scylla node and extract the IP address of the host machine by capturing the IP address from the output.

## Running Cassandra-stress

To run cassandra-stress, you can use the following command:

```bash
docker run --rm -it --network=host scylladb/cassandra-stress 'cassandra-stress write n=1000 -node $HOST_IP'
```

This will run a write test with 1000 operations on the host machine. We'll be using the host network to connect to the scylla container because it's already exposed to the host machine.
