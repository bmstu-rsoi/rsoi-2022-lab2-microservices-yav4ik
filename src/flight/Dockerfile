From python:3.8
COPY . /flight
WORKDIR /flight
COPY requirements.txt /flight/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8060
CMD gunicorn --workers=4 --bind 0.0.0.0:8060 app:app