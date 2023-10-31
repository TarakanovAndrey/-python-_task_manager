from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        help_text=_('Required field. No more than 150 characters. '
                    'Only letters, numbers and symbols @/./+/-/_.'),
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
            }
        ),
        max_length=150,

    )
    password1 = forms.CharField(
        help_text=_('Your password must contain at least 3 characters.'),
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
            }
        ),
    )
    password2 = forms.CharField(
        help_text=_('To confirm, please enter the password again.'),
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),

        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('First name'),
                    'maxlength': 150,
                    'required': True,
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Last name'),
                    'maxlength': 150,
                    'required': True,
                }
            ),
        }

    def clean_username(self):
        datas = self.cleaned_data
        users_list = User.objects.all()
        if datas['username'] in users_list.exclude(username=datas['username']):
            raise forms.ValidationError(_('A user with this name already exists.'))
        return datas['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(_("The entered passwords do not match."))
        return cd['password1']
