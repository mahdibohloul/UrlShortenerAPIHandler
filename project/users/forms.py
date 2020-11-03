from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from rest_framework.authtoken.models import Token


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError("email already token")
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(disabled=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class TokenForm(forms.ModelForm):
    key = forms.CharField(disabled=True, label='Token', required=False)

    class Meta:
        model = Token
        fields = ['key']
