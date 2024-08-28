from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom)
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
