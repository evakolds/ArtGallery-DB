from django import forms
from django.forms import ModelForm

from .models import Booking

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['exhibition', 'tickets_number']
