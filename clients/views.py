from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from formulaire.models import Client
# Create your views here.


#def client(request,pk):
    #page_client = Client.objects.get(id=pk)
    #context = {'page_client': page_client}
 #   return render(request,'clients/clients.html')


#def entreprise(request,pk):
 #   page_entreprise = Client.objects.get(id=pk)
  #  context = {'page_entreprise': page_entreprise}
   # return render(request,'clients/entreprise.html', context)
from produits.form import imageform, boutiqueform, produitForm, Albumform, Categorieform
from produits.models import Produit, Image, Boutique, Categorie, Album, Postfile


#liste des elements lier au produit
@login_required
def profil (request):
    user = request.user
    client = Client.objects.get(user=user)

    context = {'client': client}
    return render(request, 'clients/profil.html', context)


def tache(request):
    user = request.user

    # lister boutique
    listes = Boutique.objects.filter(user=user)
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        listes = Boutique.objects.filter(nom_boutiue__icontains=recherche)

    # ajouter boutique
    if request.method == 'POST':
        form = boutiqueform(request.POST, request.FILES)
        if form.is_valid():
            print("111111111111111111")
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('tache')
    else:
        form = boutiqueform()
    context = {'listes': listes, 'form': form}
    return render(request, 'clients/tache.html', context)


def image(request):
    user = request.user

    #lister les images
    listes = Image.objects.filter(user=user)
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        listes = Image.objects.filter(nom_image__icontains=recherche)

    # cree une image
    if request.method == 'POST':
        form = imageform(request.POST, request.FILES)
        if form.is_valid():
            print("111111111111111111")
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('tache')
    else:
        form = imageform()
    context = {'image': listes, 'form': form}
    return render(request, 'clients/image.html', context)


def album(request):
    user = request.user
    listes = Album.objects.filter(user=user)
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        listes = Album.objects.filter(nom_album__icontains=recherche)

    if request.method == 'POST':
        form = Albumform(request.POST, request.FILES)
        print("222222222222222222")
        if form.is_valid():
            print("111111111111111111")
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('album')
    else:
        form = Albumform()
    context = {'album': listes, 'form':form}

    return render(request, 'clients/album.html', context)

def cathegorie(request):
    user = request.user
    listes = Categorie.objects.filter(user=user)
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        listes = Categorie.objects.filter(nom_cathegorie__icontains=recherche)

        # cree un album
    if request.method == 'POST':
        form = Categorieform(request.POST, request.FILES)
        print("222222222222222222")
        if form.is_valid():
            print("111111111111111111")
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('cathegorie')
    else:
        form = Categorieform()
    context = {'listes': listes, 'form': form}
    return render(request, 'clients/cathegorie.html', context)


def produit(request):
    user = request.user
    liste_produit = Produit.objects.filter(user=user)
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        liste_produit = Produit.objects.filter(nom_produit__icontains=recherche)
    liste_image = Image.objects.all()

    #cree un produit
    if request.method == 'POST':
        form = produitForm(request.POST, request.FILES)
        print("222222222222222222")
        if form.is_valid():
            print("111111111111111111")
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('produit')
    else:
        form = produitForm()

    context = {'produits': liste_produit, 'image': liste_image, 'form': form}
    return render(request, 'clients/produit.html', context)

#supprimer les ellement lier au produit

def delet_p(request, id):
    sup = Produit.objects.filter(id=id).delete()
    return redirect('produit')


def delet_b(request, id):
    sup = Boutique.objects.filter(id=id).delete()
    return redirect('tache')


def delet_i(request, id):
    sup = Image.objects.filter(id=id).delete()
    return redirect('image')

def delet_c(request, id):
    sup = Categorie.objects.filter(id=id).delete()
    return redirect('cathegorie')


def delet_a(request, id):
    sup = Album.objects.filter(id=id).delete()
    return redirect('album')


# modifier un produit
def modifier_i(request, id):
    modify = Image.objects.get(id=id)
    form = imageform(instance=modify)
    if request.method == "POST":
        form = imageform(request.POST, instance=modify)
        if form.is_valid():
            form.save()
        return redirect('image')
    context = {'form': form}
    return render(request, 'formulaire/formulaire_client.html', context)


def modifier_p(request, id):
    modify = Produit.objects.get(id=id)
    form = produitForm(instance=modify)
    if request.method == "POST":
        form = produitForm(request.POST, instance=modify)
        if form.is_valid():
            form.save()
        return redirect('produit')
    context = {'form': form}
    return render(request, 'formulaire/formulaire_client.html', context)


def modifier_b(request, id):
    modify = Boutique.objects.get(id=id)
    form = boutiqueform(instance=modify)
    if request.method == "POST":
        form = boutiqueform(request.POST, instance=modify)
        if form.is_valid():
            form.save()
        return redirect('tache')
    context = {'form': form}
    return render(request, 'formulaire/formulaire_client.html', context)


def modifier_c(request, id):
    modify = Categorie.objects.get(id=id)
    form = Categorieform(instance=modify)
    if request.method == "POST":
        form = Categorieform(request.POST, instance=modify)
        if form.is_valid():
            form.save()
        return redirect('cathegorie')
    context = {'form': form}
    return render(request, 'formulaire/formulaire_client.html', context)

def modifier_a(request, id):
    modify = Album.objects.get(id=id)
    form = Albumform(instance=modify)
    if request.method == "POST":
        form = Albumform(request.POST, instance=modify)
        if form.is_valid():
            form.save()
        return redirect('album')
    context = {'form': form}
    return render(request, 'formulaire/formulaire_client.html', context)



