from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ['firstname', 'lastname','username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ['firstname', 'lastname','username', 'email']

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=True)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        if commit:
            user.save()
        return user

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

class PasswordUpdateForm(forms.ModelForm):
    OldPassword= forms.CharField(max_length=32, widget=forms.PasswordInput)
    NewPassword = forms.CharField(max_length=32, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'OldPassword',
            'NewPassword',
            'ConfirmPassword'
        ]