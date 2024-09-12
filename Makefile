all: check check-compose check-status install
	@echo "✅ Docker and docker-compose are installed and running"
	@echo "✅ Docker image dependencies are pulled"

.ONESHELL:

.PHONY: all check check-compose check-status install clean

# check if docker is installed
check:
	@docker --version

# check if docker-compose is installed
check-compose:
	@docker-compose --version

# check if docker is running
check-status:
	@docker info 2>/dev/null || echo "❌ Docker is not running"

# pull docker image dependencies
install:
	@docker pull scylladb/scylla || echo "❌ Docker rootless is not enabled"
	@docker pull scylladb/cassandra-stress

clean:
	@docker-compose down --rmi all --remove-orphans
	@docker rmi scylladb/cassandra-stress -f

