FROM python:3.11-slim

WORKDIR /src
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /src .
COPY .gitignore .
COPY ./instance/movies.db ../instance/

CMD flask --app app run -h 0.0.0.0 -p 80