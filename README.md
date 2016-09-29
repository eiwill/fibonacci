Fibonacci service
==================

## List of targets

##### Development run

```
make run
```
Server starts listening on port 8081

##### Docker run

```
make run-docker
```
Docker starts two containers: nginx, fibonacci.
Nginx is linked to fibonacci container and uses WSGI protocol to process requests using fibonacci container.
Nginx container listens on port 8081.

##### Build docker container

```
make build-docker
```

##### Run unit tests

```
make unit-tests
```

##### Run functional tests

```
make functional-tests
```

##### Run all tests

```
make tests
```

## Docker containers
Service consists of two containers which are connected using WSGI. 
Fibonacci service has the following environment variables:

```
# Cache type. Only memory for now, other types of cache also can be implemented: Redis cache
# or file cache
CACHE_TYPE

# Number of greenlets of fibonacci service
NUMBER_OF_THREADS

# Count of fibonacci numbers generated in one continuous loop. After each loop gevent.sleep is called 
# to switch threads
BATCH_SIZE

# Maximum numbers in fibonacci sequence that can be generated. It's depends on size of memory on machine
MAXIMUM_FIBONACCI_COUNT
```

## Docker compose structure

![project structure](/docs/fibonacci.png)