from django.db import models

# Create your models here.


class Admin(models.Model):
    fName = models.CharField(max_length=222)
    lName = models.CharField(max_length=222)

    def __str__(self):
        return self.fName


class Guest(models.Model):
    fName = models.CharField(max_length=222)
    lName = models.CharField(max_length=222)
    age = models.IntegerField()
    classroom = models.IntegerField()

    def __str__(self):
        return self.fName
