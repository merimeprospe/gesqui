from django.contrib import admin
from .models import Produit, Avis, Image, Boutique, Categorie, Album

# Register your models here.
admin.site.register(Produit)
admin.site.register(Avis)
admin.site.register(Image)
admin.site.register(Boutique)
admin.site.register(Categorie)
admin.site.register(Album)
