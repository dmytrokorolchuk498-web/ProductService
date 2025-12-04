from django.db import models
from datetime import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return f"{self.name}"