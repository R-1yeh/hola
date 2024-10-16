from django.db import models

# Create your models here.

# web/models.py
from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation by {self.name} for {self.amount}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    date = models.DateTimeField(auto_now_add=True)  # Esto agrega un campo de fecha

    
    def __str__(self):
        return self.title
