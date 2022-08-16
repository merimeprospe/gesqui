from django.urls import path
from . import views
urlpatterns = [
  path('<str:pk>', views.product, name='page_produit'),
  path('cathegorie/<pk>', views.cathegorie, name='page_cathegorie'),
    #path('product_user', views.productuser, name='product_user'),
   # path('Editimage', views.Editimage, name='Editimage'),
    #path('Editboutique', views.Editboutique, name='Editboutique'),
    #path('Editbavis', views.Editbavis, name='Editbavis'),
    #path('Editproduit', views.Editproduit, name='Editproduit'),
    #path('modifier/<pk>', views.modifier, name='modif'),
]
