From python:3.8

COPY requirements.txt /privilege/
RUN pip install --requirements /privilege/requirements.txt
COPY . /privilege
WORKDIR /privilege

EXPOSE 8050
CMD gunicorn --workers=4 --bind 0.0.0.0:8050 app:app