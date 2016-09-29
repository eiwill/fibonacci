import os

from flask import Flask, g, Response
from fibonacci.fibonacci_service import FibonacciService
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Set default config and override config from an environment variable
app.config.update(dict(
    CACHE_TYPE="memory",
    DEBUG=True,
))
app.config.from_object(os.environ.get("CONFIG_PATH", "fibonacci.config.Development"))


@app.route('/fibonacci/<count>', methods=['GET'])
def get_fibonacci_sequence(count):
    """
    Get fibonacci sequence for count of elements

    @param count: count of elements to return
    """   
    service = get_fibonacci_service()
    count = validate_count(count)

    def generate():
        yield '['
        for number in service.get_sequence(count):
            if number != 0:
                yield ','
            yield str(number)
        yield ']'
    return Response(generate(), mimetype='application/json')


def get_fibonacci_service():
    """
    Get fibonacci service
    """
    if not hasattr(g, 'fibonacci_service'):
        g.fibonacci_service = FibonacciService(app.config)
    return g.fibonacci_service


def validate_count(count):
    """
    Validate count to be int and be in range of [0, MAXIMUM_FIBONACCI_COUNT]

    @param count: count of elements in fibonacci sequence
    @return: int value

    @raises BadRequest
    """
    try:
        count = int(count)
    except ValueError:
        raise BadRequest("Value of count is not integer")

    maximum = app.config["MAXIMUM_FIBONACCI_COUNT"]
    if count < 0 or count > maximum:
        raise BadRequest("Value of count should be in range [0; %s]" % maximum)
    return count
