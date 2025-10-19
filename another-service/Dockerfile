FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
# reuse the same requirements as authentication-service for now
COPY authentication-service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY another-service/another_service /app/another_service
COPY db.py /app/db.py
COPY config /app/config
COPY models /app/models
COPY schemas /app/schemas
COPY dependencies.py /app/dependencies.py
ENV PYTHONPATH=/app
ENV APP_MODULE=another_service.main:app
EXPOSE 8000
CMD ["sh", "-c", "uvicorn $APP_MODULE --host 0.0.0.0 --port 8000 --reload"]

