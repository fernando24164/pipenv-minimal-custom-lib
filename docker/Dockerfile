FROM python:3.6-slim

RUN pip install pipenv
RUN pipenv install cython

COPY app /app
WORKDIR /app
RUN pipenv run python setup.py install

CMD python -c "import signal; signal.pause()"