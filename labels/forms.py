from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CreateLabelForm(ModelForm):

    class Meta:
        model = models.Label
        fields = ['label_name', ]
        labels = {'label_name': _('Name')}
        widgets = {
            'label_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name')
                }
            )
        }
