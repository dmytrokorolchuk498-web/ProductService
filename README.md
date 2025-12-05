Test task
Product service

# Setup:

### Docker
```docker build -t app .```
```docker compose up --build```

### Creating migration:
```docker compose exec django-web python manage.py migrate```

### Creating superuser
```docker compose exec django-web python manage.py createsuperuser``` 
