from django.db import models

# Create your models here.

class Equation (models.Model):
    id = models.BigIntegerField(primary_key=True)
    definition = models.TextField()
    def __str__(self):
        return str(id) + ": "+ str(self.definition)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
