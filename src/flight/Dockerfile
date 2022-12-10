From python:3.8
COPY requirements.txt /flight/
RUN pip install --requirements /flight/requirements.txt
COPY . /flight
WORKDIR /flight
EXPOSE 8060
CMD gunicorn --workers=4 --bind 0.0.0.0:8060 app:app