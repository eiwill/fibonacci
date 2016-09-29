import os


class Config(object):
    # Debugging mode for Flask
    DEBUG = False
    # Testing mode for Flask (unit tests)
    TESTING = False
    # Cache type. Only memory for now, other types of cache also can be implemented: Redis cache or file cache
    CACHE_TYPE = os.environ.get("CACHE_TYPE", "memory")
    # Number of greenlets of fibonacci service
    NUMBER_OF_THREADS = os.environ.get("NUMBER_OF_THREADS", 1000)
    # Count of fibonacci numbers generated in one continuous loop. After each loop gevent.sleep is called to switch
    # threads
    BATCH_SIZE = os.environ.get("BATCH_SIZE", 200)
    # Maximum numbers in fibonacci sequence that can be generated. It's depends on size of memory on machine
    MAXIMUM_FIBONACCI_COUNT = os.environ.get("MAXIMUM_FIBONACCI_COUNT", 30000)
    # Listen port for service for development mode
    LISTEN_PORT = os.environ.get("LISTEN_PORT", 8081)


class Development(Config):
    DEBUG = True


class Production(Config):
    pass
