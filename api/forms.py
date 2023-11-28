from django import forms
# from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as UserAuth


class UserRegisterForm(UserCreationForm):
 email = forms.EmailField(label='Email')
 password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
 password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
 class Meta:
		model = UserAuth
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Número de tarjeta', widget=forms.TextInput(attrs={'placeholder': '4242 4242 4242 4242'}))
    exp_month = forms.CharField(label='Mes de expiración', widget=forms.TextInput(attrs={'placeholder': 'MM'}))
    exp_year = forms.CharField(label='Año de expiración', widget=forms.TextInput(attrs={'placeholder': 'YYYY'}))
    cvc = forms.CharField(label='CVC', widget=forms.TextInput(attrs={'placeholder': '123'}))
