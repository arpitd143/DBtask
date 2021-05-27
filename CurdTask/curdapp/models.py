from django.db import models


# Create your models here.

class Employe(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact = models.IntegerField()
    salary = models.IntegerField()
    leave = models.IntegerField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UploadData(models.Model):
    file = models.FileField()