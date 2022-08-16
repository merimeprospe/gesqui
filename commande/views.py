from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from pagnier.views import getlistw, getoccurlist
from produits.models import Produit


def command(request):

    return render(request,'commande/commande.html')