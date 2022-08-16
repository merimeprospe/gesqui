import os.path
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from django.db import models


# Create your models here.
TAB = (('promo', 'promo'), ('solde', 'solde'), ('nouveau', 'nouveau'))


class Album (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='album')
    nom_album = models.CharField(max_length=30, null=True)

    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

    def __str__(self):
        return self.nom_album



class Categorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cathegorie')
    nom_cathegorie = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nom_cathegorie


class Boutique(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Boutique')
    nom_boutiue = models.CharField(max_length=30, null=True)
    lieu_boutique = models.CharField(max_length=40, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_boutiue


class Produit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Produit')
    boutique = models.ManyToManyField(Boutique)
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    nom_produit = models.CharField(max_length=100, null=True)
    quantité_produit = models.IntegerField(null=True)
    prix_promo = models.IntegerField(blank=True, default=0000)
    prix_produit = models.IntegerField(null=True)
    cathegorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=TAB, blank=True, default='nouveau')
    description_du_produit = models.CharField(max_length=10000, blank=True, default=" ")
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_produit


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Postfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner')
    file = models.FileField(upload_to=user_directory_path)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image')
    nom_image = models.CharField(max_length=255)
    #image = models.ManyToManyField(Postfile, related_name='image')
    image = models.ImageField(null=True, upload_to='image/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_image


class Avis (models.Model):
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    nom = models.CharField(max_length=30, null=True)
    adresse_email = models.EmailField(null=True)
    avis = models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


