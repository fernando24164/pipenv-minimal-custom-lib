FROM python:3.6-slim

RUN pip install pipenv
RUN pipenv install cython

CMD python -c "import signal; signal.pause()"