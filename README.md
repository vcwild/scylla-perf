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

The CLI works by encapsulating all of its dependencies in docker containers, so having [docker](https://docs.docker.com/engine/install/), [rootless-mode](https://docs.docker.com/engine/security/rootless/) access, and [docker-compose](https://docs.docker.com/compose/install/) installed are the only requirements.

This project **only supports Linux-based systems**.

## Table of Contents

- [Requirements](#requirements)
- [Sanity Checks](#sanity-checks)
- [Manual Configuration](#manual-configuration)
- [Running the Performance Test](#running-the-performance-test)
- [Cleanup](#cleanup)
- [License](#license)

## Requirements

- [Make](https://www.gnu.org/software/make/)
- [Docker](https://docs.docker.com/engine/install/)
- [Rootless Docker](https://docs.docker.com/engine/security/rootless/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [ScyllaDB image](https://hub.docker.com/r/scylladb/scylla/)
- [Cassandra-stress image](https://hub.docker.com/r/scylladb/cassandra-stress)

## Sanity Checks

To verify if all project dependencies are installed, you can run the following command:

```bash
make
```

This will verify if `docker` and `docker-compose` are installed and will automatically pull the required container images.
The make command **does NOT** install [docker](https://docs.docker.com/engine/install/) or [docker-compose](https://docs.docker.com/compose/install/). You need to install them manually and give docker [rootless-mode](https://docs.docker.com/engine/security/rootless/) access.

If all sanity checks pass, you can skip to the [running the performance test](#running-the-performance-test) section.

## Manual Configuration

Only use the manual installation to troubleshoot if the [sanity checks](#sanity-checks) failed.

<details close>
<summary>Click to expand</summary>

### Deploying a ScyllaDB cluster

To deploy a single node ScyllaDB cluster, you can use the following command:

```bash
docker-compose up -d
```

This will create a scylla service using the scylladb/scylla image. The service will be named `some-scylla` and will be running in the background.

You can check the logs by running:

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

If these steps are successful, you can proceed to run the performance test.

</details>

## Running the Performance Test

Before running the performance test, you should make sure to pass the [sanity checks](#sanity-checks).

To run the performance test, you should first give execute permission to the CLI program.

```bash
chmod +x scylla-perf
```

Add the current program directory to the PATH environment variable.

```bash
export PATH=$PATH:$(pwd)
```

To run the CLI program simply use the `scylla-perf` command and follow the instructions on the screen.

The first time you run the program, it will instantiate the ScyllaDB database cluster.

After the configuration is done, you can run any cassandra-stress test on the cluster.

```bash
scylla-perf N
```

Where `N` is the number of cassandra-stress tests you want to run.

## Cleanup

To clean up the resources created by the program, you can run the following command:

```bash
make clean
```

## License

This project is licensed under the Apache License License - see the [LICENSE](LICENSE) file for details.
