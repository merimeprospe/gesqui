from django.db import models
from produits.models import Produit
# Create your models here.


class Panier (models.Model):
    produit = models.ManyToManyField(Produit)
    quantie = models.IntegerField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.produit