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

up-compose:
	@docker-compose up -d

# pull docker image dependencies
pull: check
	@docker pull scylladb/scylla
	@docker pull scylladb/cassandra-stress

# pull docker images and start the scyllaDB container
install: pull up-compose

.PHONY: all check check-compose check-status pull up-compose install
