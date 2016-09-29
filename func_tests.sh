cleanup() {
  docker-compose kill
  docker-compose rm -f
	trap - EXIT
}

trap cleanup INT TERM EXIT

docker-compose up -d

sleep 2

env/bin/nosetests tests/functional -v