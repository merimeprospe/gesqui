from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def servise(request):
    return render(request,'service/service.html')