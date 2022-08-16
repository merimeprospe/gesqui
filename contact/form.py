from django import forms

from contact.models import Message


class contactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('nom', 'prenom', 'adresse_email', 'tel', 'message')
