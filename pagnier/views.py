from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from produits.models import Produit
from django import template


def getlistw(l):
    listocc=[]
    for k in l:
       if k  not in listocc:
        listocc.append(k)
    return listocc


def getoccurlist(l):
    wlist=getlistw(l)
    occur=[]
    for k in wlist:
        occur.append(l.count(k))
    return  occur


register = template.Library()

def basket(request):
    if "items" in request.GET.keys():
        it = request.GET["items"]
        if it:
            items_id = it.split(',')
            Items = []
            for k in items_id:
                Items.append(Produit.objects.get(id=int(k)))
            dlist = getlistw(Items)
            occurs = getoccurlist(Items)
            z = zip(dlist, occurs)
            p=[]
            for i,k in z:
                p.append(i.prix_produit*k)
            s=0.0
            for i in p:
                s+=i
            z=zip(dlist,occurs,p)

    return render(request,'pagneir/pagnier.html', locals())
