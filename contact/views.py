from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from contact.form import contactForm
from django.shortcuts import render, redirect


def contact(request):
    form = contactForm()
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            adresse_email = form.cleaned_data.get('adresse_email')
            tel = form.cleaned_data.get('tel')
            message = form.cleaned_data.get('message')
            form.save()
            return redirect('contact')
    context = {'form': form}
    return render(request, 'contact/contact.html', {'form': form})
