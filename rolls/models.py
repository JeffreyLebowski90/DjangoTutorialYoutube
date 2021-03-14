from django.db import models


class Roll(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField()