from django.db import models
from formulaire.models import Client
from produits.models import Produit
# Create your models here.


class Commande (models.Model):
    status = (('non livré', 'non livré'), ('livré', 'livré'))
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    quantité_commande = models.IntegerField(null=True)
    total_commande = models.IntegerField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numeroCommande


class Livraison (models.Model):
    PriX_Livraison = models.IntegerField(null=True)
    lieu_Livraison = models.CharField(max_length=100,null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lieu_Livraison


