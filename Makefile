all: check check-compose check-status pull

# check if docker is installed
check:
	@docker --version

# check if docker-compose is installed
check-compose:
	@docker-compose --version

# check if docker is running
check-status:
	@docker info

# pull docker image dependencies
pull: check
	@docker pull scylladb/scylla
	@docker pull scylladb/cassandra-stress

.PHONY: all check check-compose check-status pull
