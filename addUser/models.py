from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
