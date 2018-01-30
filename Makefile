.PHONY: freeze test dist

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

test:
	python test.py

dist:
	python setup.py sdist
