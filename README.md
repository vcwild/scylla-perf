<div align="center">
  <img src=".github/assets/image.png" width="230px" />
</div>
<br/>
<div align="center">
  <img src="https://img.shields.io/github/languages/count/vcwild/scylla-perf?color=%234466fb&style=flat-square" alt="languages" />
  <img src="https://img.shields.io/github/license/vcwild/scylla-perf?color=%234466fb&style=flat-square" alt="license" />
  <img src="https://img.shields.io/github/repo-size/vcwild/scylla-perf?color=%234466fb&style=flat-square" alt="repo size" />
  <img src="https://img.shields.io/github/actions/workflow/status/vcwild/scylla-perf/build.yml?branch=main&style=flat-square&color=%234466fb" alt="build" />
</div>

# scylla-perf

Scylla-perf is a CLI program that is used to run performance testing on a ScyllaDB cluster.

## Table of Contents

- [Requirements](#requirements)
- [Sanity Checks](#sanity-checks)
- [Configuration](#configuration)
  - [Deploying a ScyllaDB cluster](#deploying-a-scylladb-cluster)
  - [Finding the host IP](#finding-the-host-ip)
  - [Running a Cassandra-stress](#running-a-cassandra-stress)
  - [Configuring the CLI program](#configuring-the-cli-program)
- [Running the performance test](#running-the-performance-test)

## Requirements

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [ScyllaDB image](https://hub.docker.com/r/scylladb/scylla/)
- [Cassandra-stress image](https://hub.docker.com/r/scylladb/cassandra-stress)

## Sanity Checks

To verify if all project dependencies are installed, you can run the following command:

```bash
make
```

This will verify if `docker` and `docker-compose` are installed and will automatically pull the required container images.
The make command **does NOT** install [docker](https://docs.docker.com/engine/install/) or [docker-compose](https://docs.docker.com/compose/install/). You need to install them manually.

## Configuration

The following steps are required to configure the CLI.

### Deploying a ScyllaDB cluster

To deploy a single node ScyllaDB cluster, you can use the following command:

```bash
docker-compose up -d
```

This will create a scylla service using the scylladb/scylla image. The service will be named `some-scylla` and will be running in the background.

The container will be running in the background. You can check the logs by running:

```bash
docker logs some-scylla | tail
```

### Finding the host IP

The host machine IP address is required to run the cassandra-stress test.

To find the IP address of the host machine, you can run the following command:

```bash
export HOST_IP=$(docker exec -it some-scylla nodetool status | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b")
```

This will use the node tool to get the status of the scylla node and extract the IP address of the host machine by capturing the IP address from the output.

### Running a Cassandra-stress

To run cassandra-stress sanity test, you can use the following command:

```bash
docker run --rm -it --network=host scylladb/cassandra-stress 'cassandra-stress write duration=10s -rate threads=10 -node $HOST_IP'
```

This will run a write test with 1000 operations on the host machine. We'll be using the host network to connect to the scylla container because it's already exposed to the host machine.

### Configuring the CLI program

To run the performance test, you should first give execute permission to the CLI program.

```bash
chmod +x scylla-perf
```

Add the current program directory to the PATH environment variable.

```bash
export PATH=$PATH:$(pwd)
```

If all the steps above were successful, the CLI should be configured and ready to run the performance test.

## Running the performance test

Before running the performance test, you should make sure to pass the [sanity checks](#sanity-checks) and all [configuration](#configuration) steps.

To run the CLI program simply use the `scylla-perf` command and follow the instructions on the screen.
