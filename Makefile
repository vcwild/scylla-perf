define task =
if grep -q docker /etc/group
then
		touch .rootless
		echo "Docker group already exists"
else
		sudo groupadd docker
fi
sudo usermod -aG docker $$USER
endef

all: check check-compose check-status install

.ONESHELL:

.PHONY: all check check-compose check-status install clean

.rootless:
	@$(task)

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
install: .rootless
	@docker pull scylladb/scylla
	@docker pull scylladb/cassandra-stress

clean:
	@docker-compose down --rmi all --remove-orphans
	@docker rmi scylladb/cassandra-stress -f
	@rm -f .rootless

