FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app

RUN set -ex; \
    pip install -r requirements.txt; \
    rm -rf /root/.cache; \
    apt-get update && \
    apt-get install -y libpq-dev gcc

CMD ["python3", "server.py"]
