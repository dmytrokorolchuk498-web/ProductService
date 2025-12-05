FROM python:3.13.10-slim-bookworm

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean   

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]