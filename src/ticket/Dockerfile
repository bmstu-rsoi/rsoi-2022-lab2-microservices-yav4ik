From python:3.8
COPY . /ticket
COPY requirements.txt /privilege
WORKDIR /ticket
RUN pip install -r requirements.txt
EXPOSE 8070
CMD gunicorn --workers=4 --bind 0.0.0.0:8070 app:app