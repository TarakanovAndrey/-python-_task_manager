from django import forms
from django.forms import ModelForm
from . models import CustomUser
from django.utils.translation import gettext_lazy as _


class UserLoginForm(forms.Form):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Username'),
    }))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': _('Password'),
    }))


class CustomUserCreationForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password',
                  'password_confirmation']
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'username': _('Username'),
            'password': _('Password'),
            'password_confirmation': _('Password confirmation')
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['first_name']
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['last_name']}),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['username']}),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['password']}),
            'password_confirmation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['password_confirmation']}),
            # '332': forms.PasswordInput() посмотреть на замену для password

        }
