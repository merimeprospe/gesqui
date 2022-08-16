from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from produits.models import Produit, Categorie, Image


def cathegorie(request, pk):
    image = Image.objects.all()
    cathegorie1 = Categorie.objects.all()
    produits = Produit.objects.filter(cathegorie__id=pk)
    pagination = Paginator(produits, 12)
    page = request.GET.get('page')
    produits = pagination.get_page(page)
    context = {'produit': produits, 'image': image, 'cathegorie1': cathegorie1}
    print(context)
    return render(request, 'produits/cathegorie.html', context)

