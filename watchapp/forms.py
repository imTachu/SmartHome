from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from models import UserProfile

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileForm(forms.Form):
	mobile_number = forms.CharField(label='Celular', max_length=15, required=True)
	email = forms.EmailField(label='Correo', required=True)
	file = forms.ImageField(label='Foto', required=True)

