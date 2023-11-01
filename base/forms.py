from django import forms
from django.utils.translation import gettext_lazy as _


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
            }
        ),
        max_length=150,
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
            }
        ),
    )
