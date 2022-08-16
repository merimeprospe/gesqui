from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


# Create your views here.


# def inscriptionpage_Client(request):
#     form = CreerUtilisateur()
#     if request.method == 'POST':
#         form = CreerUtilisateur(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('client')
#     context = {'form': form}
#     return render(request, 'formulaire/inscription_client.html', context)
#
#
# def inscriptionpage_Entreprise(request):
#     form = CreerUtilisateur()
#     if request.method == 'POST':
#         form = CreerUtilisateur(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('entreprise')
#     context = {'form': form}
#     return render(request, 'formulaire/inscription.html', context)
#
#
# def formulaire(request):
#     if request.method == "POST":
#         form = Entrepriseform(request.POST).save()
#         return redirect('/')
#     else:
#         form = Entrepriseform()
#         return render(request, 'formulaire/formulaire.html', {'form': form})
#
#
# def formulaire_client(request):
#     print(1)
#     user = request.user
#     if request.method == 'POST':
#         form = Clientsform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = Clientsform()
#         return render(request, , {'form': form})
from formulaire.formulaire import SignupForm, EditclientForm
from formulaire.models import Client

@login_required
def Editclient(request):
    user = request.user.id
    client = Client.objects.get(user__id=user)

    if request.method == 'POST':
        form = EditclientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            client.nom = form.cleaned_data.get('nom')
            client.prenom = form.cleaned_data.get('prenom')
            client.telephone = form.cleaned_data.get('telephone')
            client.banquaire = form.cleaned_data.get('banquaire')
            client.OM = form.cleaned_data.get('OM')
            client.MOMO = form.cleaned_data.get('MOMO')
            client.save()
            return redirect('dashboard')
    else:
        form = EditclientForm(instance=client)

    context = {
        'form': form,
    }

    return render(request, 'formulaire/formulaire_client.html', context)

