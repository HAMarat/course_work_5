FROM python:3.11-slim

WORKDIR /
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./scp
COPY .gitignore .

CMD flask --app ./scp/app run -h 0.0.0.0 -p 80