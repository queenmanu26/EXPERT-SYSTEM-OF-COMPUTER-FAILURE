from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=254)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
		self.fields['first_name'].widget.attrs['placeholder'] = 'Prénom'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Nom'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmation de mot de passe'

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'