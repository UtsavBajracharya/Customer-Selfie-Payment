from django import forms
from django.contrib.auth.models import User
from users.models import AppUser
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class AppUserRegister(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ['phone']

class LoginForm(forms.Form):
    username= forms.CharField(label="Username")
    password= forms.CharField(label='Password', widget=forms.PasswordInput)


class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

