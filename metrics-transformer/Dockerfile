FROM python:3.13-slim
LABEL authors="ahmedwerghi"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python3", "main.py"]