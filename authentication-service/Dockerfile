FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
# requirements live in authentication-service
COPY authentication-service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# copy service code and shared db module from repo root
COPY authentication-service/authentication_service /app/authentication_service
COPY db.py /app/db.py
COPY config /app/config
COPY models /app/models
COPY schemas /app/schemas
COPY dependencies.py /app/dependencies.py
ENV PYTHONPATH=/app
ENV APP_MODULE=authentication_service.main:app
EXPOSE 8000
CMD ["sh", "-c", "uvicorn $APP_MODULE --host 0.0.0.0 --port 8000 --reload"]


