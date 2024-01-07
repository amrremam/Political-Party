from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    Approve = models.BooleanField(default=False)

    def __str__(self):
        return self.name
