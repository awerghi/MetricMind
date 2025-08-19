FROM python:3.13-slim
LABEL authors="ahmedwerghi"


WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --only-binary :all: psycopg2-binary

ENTRYPOINT ["python3", "main.py"]