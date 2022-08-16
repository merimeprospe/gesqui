from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.db.models.signals import post_save



# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    nom = models.CharField(max_length=30, null=True)
    prenom = models.CharField(max_length=30, null=True)
    telephone = models.IntegerField(null=True)
    banquaire = models.IntegerField(null=True)
    OM = models.IntegerField(null=True, blank=True)
    MOMO = models.IntegerField(null=True, blank=True)
    client_simple = 'client_simple'
    client_entreprise = 'client_entreprise'
    user_types = [(client_simple, 'client_simple'), (client_entreprise, 'client_entreprise')]
    user_type = models.CharField(max_length=20, choices=user_types, default=client_simple, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

   # def __str__(self):
    #    return self.user or ''


def create_user_profile(sender, instance, created, **Kwargs):
    if created:
        Client.objects.create(user=instance)


def save_user_profile(sender, instance, **Kwargs):
    instance.client.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)