FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# requirements лежит в папке app/
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# код Django лежит в папке app/
COPY app /app

# entrypoint лежит в docker/scripts
COPY scripts/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//' /entrypoint.sh && chmod +x /entrypoint.sh

EXPOSE 8082

ENTRYPOINT ["sh", "/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]