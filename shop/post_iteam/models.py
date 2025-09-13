from django.db import models

# Create your models here.

class post_iteam(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    img  = models.ImageField()
    price = models.CharField(max_length=100_000_000_000)
    code = models.CharField(max_length=4)

    