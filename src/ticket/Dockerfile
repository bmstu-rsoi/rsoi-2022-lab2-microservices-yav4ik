From python:3.8

COPY requirements.txt /ticket/
RUN pip install --requirements /ticket/requirements.txt
COPY . /ticket
WORKDIR /ticket

EXPOSE 8070
CMD gunicorn --workers=4 --bind 0.0.0.0:8070 app:app