FROM python:3.11-alpine3.19

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8080

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8080"]
