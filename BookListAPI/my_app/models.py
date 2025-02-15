from django.db import models

# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=5,decimal_places=2)
    Inventory=models.PositiveSmallIntegerField()
    