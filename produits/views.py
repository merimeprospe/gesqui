from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .form import produitForm, imageform, boutiqueform, avisform
from .models import Produit, Image, Boutique, Avis, Categorie


# Create your views here.

@login_required
def modifier(request, pk):
    user = request.user.id
    produit = Produit.objects.get(user__id=user)
    modify = Produit.objects.get(id=pk)
    form = produitForm(instance=modify)
    if request.method == "POST":
        form = produitForm(request.POST, instance=modify)
        if form.is_valid():
            produit.nom_produit = form.cleaned_data.get('nom_produit')
            produit.prix_produit = form.cleaned_data.get('prix_produit')
            produit.quantité_produit = form.cleaned_data.get('quantité_produit')
            produit.description_du_produit = form.cleaned_data.get('description_du_produit')
            produit.album = form.cleaned_data.get('album')
            produit.boutique = form.cleaned_data.get('boutique')
            produit.cathegorie = form.cleaned_data.get('cathegorie')
            produit.prix_promo = form.cleaned_data.get('prix_promo')
            produit.status = form.cleaned_data.get('status')
            produit.save()
            form.save()
        return redirect('tache')
    context = {'form': form}
    return render(request, 'formulaire/formulaire.html', context)


def product(request, pk):
    user = request.user.id
    produits = Produit.objects.get(id=pk)
    connexes = Produit.objects.filter(cathegorie=produits.cathegorie)
    pagination = Paginator(connexes, 4)
    page = request.GET.get('page')
    connexes = pagination.get_page(page)
    avis = produits.avis_set.all()
    pagination = Paginator(avis, 2)
    page = request.GET.get('page')
    avis = pagination.get_page(page)
    #ajouter un avie
    form = avisform()
    if request.method == 'POST':
        form = avisform(request.POST, request.FILES)
        print("222222222222222222")
        if form.is_valid():
            print("111111111111111111")
            form.save()
            return redirect('boutique')
    else:
        form = avisform()

    liste_image = Image.objects.all()
    context = {'produit': produits, 'image': liste_image, 'connexe': connexes, 'form': form, 'avis': avis}
    return render(request, 'produits/produits.html', context)


def cathegorie(request, pk):
    image = Image.objects.all()
    print(1111111111111111111111);
    cathegorie = Categorie.objects.filter(id=pk)
    cathegorie1 = Categorie.objects.all()
    produits = Produit.objects.filter(cathegorie__id=pk)
    pagination = Paginator(produits, 12)
    page = request.GET.get('page')
    produits = pagination.get_page(page)
    print(22222222222222222222222222);
    context = {'produit': produits, 'image': image, 'cathegorie': cathegorie, 'cathegorie1': cathegorie1}
    print(context)
    return render(request, 'produits/cathegorie.html', context)


@login_required
def Editimage(request):
    user = request.user.id
    image = Image.objects.get(user__id=user)
    if request.method == 'POST':
        form = imageform(request.POST, request.FILES, instance=image)
        if form.is_valid():
            image.image = form.cleaned_data.get('image')
            image.album = form.cleaned_data.get('album')
            image.default = form.cleaned_data.get('default')
            image.width = form.cleaned_data.get('width')
            image.length = form.cleaned_data.get('length')
            image.save()
            return redirect('/')
    else:
        form = imageform(instance=image)

    context = {
        'form': form,
    }

    return render(request, 'formulaire/formulaire_client.html', context)


@login_required
def Editboutique(request):
    user = request.user.id
    boutique = Boutique.objects.get(user__id=user)

    if request.method == 'POST':
        form = boutiqueform(request.POST, request.FILES, instance=boutique)
        if form.is_valid():
            boutique.nom_boutique = form.cleaned_data.get('nom_boutiue')
            boutique.lieu_boutique = form.cleaned_data.get('lieu_boutique')
            boutique.save()
            return redirect('/')
    else:
        form = boutiqueform(instance=boutique)

    context = {
        'form': form,
    }

    return render(request, 'formulaire/formulaire_client.html', context)


@login_required
def Editbavis(request):
    user = request.user.id
    avis = Avis.objects.get(user__id=user)

    if request.method == 'POST':
        form = avisform(request.POST, request.FILES, instance=avis)
        if form.is_valid():
            avis.nom = form.cleaned_data.get('nom')
            avis.adresse_email = form.cleaned_data.get('adresse_email')
            avis.avis = form.cleaned_data.get('avis')
            avis.save()
            return redirect('/')
    else:
        form = avisform(instance=avis)

    context = {
        'form': form,
    }

    return render(request, 'formulaire/formulaire_client.html', context)


@login_required
def Editproduit(request):
    user = request.user.id
    produit = Produit.objects.get(user__id=user)
    if request.method == 'POST':
        form = produitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            produit.nom_produit= form.cleaned_data.get('nom_produit')
            produit.prix_produit= form.cleaned_data.get('prix_produit')
            produit.quantité_produit = form.cleaned_data.get('quantité_produit')
            produit.description_du_produit = form.cleaned_data.get('description_du_produit')
            produit.album = form.cleaned_data.get('album')
            produit.boutique = form.cleaned_data.get('boutique')
            produit.cathegorie = form.cleaned_data.get('cathegorie')
            produit.prix_promo = form.cleaned_data.get('prix_promo')
            produit.status = form.cleaned_data.get('status')
            produit.save()
            return redirect('/')
    else:
        form = produitForm(instance=produit)

    context = {
        'form': form,
    }

    return render(request, 'formulaire/formulaire.html', context)


