from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUp(UserCreationForm):
	first_name=forms.CharField(max_length=50)
	second_name=forms.CharField(max_length=50)
	email=forms.EmailField()

	class Meta:
		fields=('username', 'password1', 'password2', 'first_name', 'second_name', 'email')
		model=User