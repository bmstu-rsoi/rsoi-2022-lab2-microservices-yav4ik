From python:3.8
COPY . /privilege
WORKDIR /privilege
COPY requirements.txt /privilege/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8050
CMD gunicorn --workers=4 --bind 0.0.0.0:8050 app:app