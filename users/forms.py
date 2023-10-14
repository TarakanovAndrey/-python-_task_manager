from django import forms
from django.forms import ModelForm
from . models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'nickname', 'password', 'password_confirmation']
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'nickname': _('Nickname'),
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
            'nickname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['nickname']}),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['password']}),
            'password_confirmation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': labels['password_confirmation']}),

        }
