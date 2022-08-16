from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return render(request,'A_propos/A_propos.html')