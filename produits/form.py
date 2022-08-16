from django.forms import ModelForm
from django import forms
from .models import Produit, Boutique, Image, Avis, Categorie, Album


class produitForm(ModelForm):

    class Meta:
        model = Produit
        fields = [ 'boutique', 'nom_produit', 'quantité_produit', 'prix_promo', 'prix_produit', 'cathegorie', 'album', 'status', 'description_du_produit']


class imageform(ModelForm):
    class Meta:
        model = Image
        fields = ['nom_image', 'default', 'width', 'length', 'album']


class boutiqueform(ModelForm):
    nom_boutiue = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    lieu_boutique = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    class Meta:
        model = Boutique
        fields = ['nom_boutiue', 'lieu_boutique']


class avisform(ModelForm):

    class Meta:
        model = Avis
        fields = ['produit', 'nom', 'adresse_email', 'avis']


class Categorieform(ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom_cathegorie']

class Albumform(ModelForm):
    class Meta:
        model = Album
        fields = ['nom_album']