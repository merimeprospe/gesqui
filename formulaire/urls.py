from django.urls import path
from . import views\

urlpatterns = [
    path('entreprise', views.Editclient, name='entreprise'),
    # path('client', views.formulaire_client, name='client'),
    # path('user_client', views.inscriptionpage_Client, name='user_client'),
    # path('user_entreprise', views.inscriptionpage_Entreprise, name='user_entreprise'),
]