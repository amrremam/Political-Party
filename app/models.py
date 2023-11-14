from django.db import models

# Create your models here.


class District(models.Model):
    label = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)