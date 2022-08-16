from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Message (models.Model):
    nom = models.CharField(max_length=30, null=True)
    prenom = models.CharField(max_length=30, null=True)
    adresse_email = models.EmailField(null=True)
    tel = models.IntegerField(null=True)
    message = models.CharField(max_length=300, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
