from django import forms
from django.contrib.auth.models import User

from .models import Book
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm


class PostBook (forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'book', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form'}),
            'author': forms.TextInput(attrs={'class':'form'}),
            'book': forms.FileInput(attrs={'class':'form'}),
            # 'category': forms.Input(attrs={'class':'form'})
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

