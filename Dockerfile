FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --settings=stripe_backend.settings

EXPOSE 8000

CMD ["gunicorn", "stripe_backend.wsgi:application", "--bind", "0.0.0.0:$PORT"]