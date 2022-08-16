from django.urls import path
from . import views
urlpatterns = [
    #path('<str:pk>', views.client, name='page_client'),
   # path('<str:pk>', views.entreprise, name='page_entreprise'),
    path('tache', views.tache, name='tache'),
    path('supprime/<id>', views.delet_p, name='delet_p'),
    path('supprime_b/<id>', views.delet_b, name='delet_b'),
    path('supprime_c/<id>', views.delet_c, name='delet_c'),
    path('supprime_a/<id>', views.delet_a, name='delet_a'),
    path('supprime_i/<id>', views.delet_i, name='delet_i'),
    path('produit', views.produit, name='produit'),
    path('cathegorie', views.cathegorie, name='cathegorie'),
    path('album', views.album, name='album'),
    path('image', views.image, name='image'),
    path('profil', views.profil, name='profil'),
    path('modifier_a/<id>', views.modifier_a, name='modifier_a'),
    path('modifier_c/<id>', views.modifier_c, name='modifier_c'),
    path('modifier_b/<id>', views.modifier_b, name='modifier_b'),
    path('modifier_p/<id>', views.modifier_p, name='modifier_p'),
    path('modifier_i/<id>', views.modifier_i, name='modifier_i'),

 ]