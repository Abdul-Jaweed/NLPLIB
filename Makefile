install:
	pip install --upgrade pip && \
		pip install -r requirements.txt
		python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=wikiphrases --cov=nlplib test_corenlp.py

lint:
	pylint --disable=R,C *.py nlplib/*.py


format:
	black *.py nlplib


all: install lint test format