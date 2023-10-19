from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CreateStatusForm(ModelForm):

    class Meta:
        model = models.Status
        fields = ['status_name',]
        labels = {'status_name': _('Name')}
        widgets = {
            'status_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name')
                }
            )
        }

