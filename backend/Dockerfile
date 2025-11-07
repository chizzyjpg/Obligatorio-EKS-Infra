FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir django djangorestframework django-cors-headers python-dotenv

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
