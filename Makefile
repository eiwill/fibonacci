all: run

env: requirements.txt
	@bash -c "virtualenv env"

main-deps: env
	env/bin/pip install -r requirements.txt

test-deps: main-deps requirements-test.txt
	env/bin/pip install -r requirements-test.txt

run: main-deps
	@bash -c "env/bin/python main.py"

run-docker:
	@docker-compose up

clean:
	rm -rf env && find ./ -name "*.pyc" | xargs rm

unit-tests: test-deps
	@bash -c "env/bin/nosetests -v tests/unit"

functional-tests: test-deps
	@bash func_tests.sh

tests: unit-tests functional-tests

build-docker:
	@bash -c "docker build -t fibonacci -f Dockerfile ."

.PHONY: run
