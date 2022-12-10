From python:3.8
COPY . /ticket
WORKDIR /ticket
COPY requirements.txt /privilege/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8070
CMD gunicorn --workers=4 --bind 0.0.0.0:8070 app:app