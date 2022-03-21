from django.db import models

# Create your models here.
class Corporates(models.Model):
    org=models.CharField(max_length=255)
    nature=models.CharField(max_length=255)
    opennings=models.TextField()
    place=models.CharField(max_length=255)
    employees=models.IntegerField()
    basic=models.DecimalField(max_digits=3,decimal_places=2)
    ratings=models.DecimalField(max_digits=3,decimal_places=2)
    
    class Meta:
        db_table="corporates"