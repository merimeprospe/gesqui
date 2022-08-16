from django.urls import path
from . import views
urlpatterns = [
  path('<str:pk>', views.cathegorie, name='page_cathegorie1'),
]
