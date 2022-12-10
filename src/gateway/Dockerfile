From python:3.8
COPY requirements.txt /gateway/
RUN pip install --requirements /gateway/requirements.txt
COPY . /gateway
WORKDIR /gateway

EXPOSE 8080
CMD gunicorn --workers=4 --bind 0.0.0.0:8080 app:app