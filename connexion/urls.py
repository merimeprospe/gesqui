from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .views import Dashboardview

urlpatterns = [
    path('', views.Login, name='connexion'),
    path('dashboard', view=Dashboardview, name='dashboard'),
    path('logout', view=LogoutView.as_view(), name='logout'),

]