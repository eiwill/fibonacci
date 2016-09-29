import gevent

from gevent.pool import Pool


class FibonacciService(object):
    """
    Fibonacci service is used to get fibonacci sequence
    """

    def __init__(self, config):
        """
        @param config: service configuration
        """
        batch_size = config["BATCH_SIZE"]
        if config["CACHE_TYPE"] == "memory":
            self.fibonacci = MemoryCachedFibonacci(batch_size)

        # It is also possible to implement file cache or Redis cache.

        self.threads_pool = Pool(config["NUMBER_OF_THREADS"])

    def get_sequence(self, count):
        """
        Get fibonacci sequence
        @param count: count of elements to return
        @return: generator for fibonacci sequence
        """
        return self.threads_pool.apply(self.fibonacci.get_sequence, [count])


class CachedFibonacci(object):
    """
    Base class for cached fibonacci sequence
    """
    def __init__(self, batch_size):
        """
        @param batch_size: count of fibonacci numbers generated in one continuous loop
        """
        self.batch_size = batch_size

    def get_sequence(self, count):
        """
        Get fibonacci sequence
        @param count: count of elements to return
        """
        raise NotImplementedError()

    def switch_context(self, counter):
        """
        Switch between threads each N elements
        @param counter: current element number
        """
        if counter > 0 and counter % self.batch_size == 0:
            gevent.sleep(0)


class MemoryCachedFibonacci(CachedFibonacci):
    """
    Memory cached fibonacci
    """
    def __init__(self, batch_size):
        """
        @param batch_size: count of fibonacci numbers generated in one continuous loop
        """
        super(MemoryCachedFibonacci, self).__init__(batch_size)
        self.memory = [0, 1]

    def get_sequence(self, count):
        """
        Get fibonacci sequence
        @param count: count of elements to return
        @return: generator for fibonacci sequence
        """
        counter = 0

        for number in self.memory[:count]:
            counter += 1
            self.switch_context(counter)

            yield number

        if len(self.memory) < count:
            for i in xrange(count - len(self.memory)):
                n = self.memory[-2] + self.memory[-1]
                self.memory.append(n)
                self.switch_context(i)
                yield n
