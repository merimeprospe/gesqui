from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.views.generic import TemplateView

# Create your views here.
from formulaire.formulaire import SignupForm, ChangePasswordForm
from produits.models import Produit,Image


def Login(request):
    form1 = SignupForm()
    if request.method == 'POST':
        form1 = SignupForm(request.POST)
        if form1.is_valid():
            print("222222222")
            username = form1.cleaned_data.get('username')
            email = form1.cleaned_data.get('email')
            password = form1.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('connexion')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('dashboard')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    print("111111111111111111111111")
    return render(request, 'connexion/connexion.html', {'form': form, 'title': 'log in', 'form1': form1})


@login_required
def Dashboardview(request):
    user = request.user.id
    liste_produit = Produit.objects.filter(user=user)
    recherche = request.GET.get('recherche')
    if recherche != '' and recherche is not None:
        liste_produit = Produit.objects.filter(nom_produit__icontains=recherche)
    liste_image = Image.objects.all()
    context = {'produits': liste_produit, 'image': liste_image}
    return render(request, 'clients/entreprise.html', context)


def userform(request):


    return render(request, 'connexion/connexion.html', context)

@login_required
def PasswordChange(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'registration/change_password.html', context)


def PasswordChange(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'registration/change_password.html', context)


def PasswordChangeDone(request):
    return render(request, 'change_password_done.html')