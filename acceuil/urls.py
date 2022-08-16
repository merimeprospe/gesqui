from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='acceuil'),
    path('boutique', views.boutique, name='boutique'),
]
