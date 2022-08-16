from django.core.paginator import Paginator
from django.shortcuts import render
from produits.models import Produit, Image, Categorie
from django.http import HttpResponse
# Create your views here.


def home(request):
    liste_image = Image.objects.all()
    liste_produit1 = Produit.objects.all()
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        liste_produit1 = Produit.objects.filter(nom_produit__icontains=recherche)
    liste_produit = Produit.objects.filter(status="nouveau")
    liste_produit2 = Produit.objects.filter(status="solde")
    context = {'produits': liste_produit, 'image': liste_image, 'produits1': liste_produit2, 'produits2': liste_produit1}
    return render(request, 'acceuil/acceuil.html', context)


def boutique(request):
    cathegorie = Categorie.objects.all()
    liste_produit = Produit.objects.all()
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        liste_produit = Produit.objects.filter(nom_produit__icontains=recherche)
    pagination = Paginator(liste_produit, 12)
    page = request.GET.get('page')
    liste_produit = pagination.get_page(page)
    liste_image = Image.objects.all()
    #for imag in liste_image :
    context = {'produits': liste_produit, 'image': liste_image, 'cathegorie': cathegorie}
    return render(request, 'acceuil/boutique.html', context)








