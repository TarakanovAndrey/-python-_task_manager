from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class TaskCreateForm(ModelForm):

    class Meta:
        model = models.Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name'),
                    'required': True,
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Description'),
                    'required': False,
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': _('Status'),
                    'required': True,
                }
            ),
            'executor': forms.Select(
                attrs={
                    'class': 'form-select',
                    'required': False,
                }
            ),
            'labels': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'required': False,
                }
            )
        }


class TasksFilterForm(ModelForm):

    class Meta:
        model = models.Task
        fields = ['status', 'executor', 'labels', ]
        labels = {
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
        widgets = {
            'status': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'executor': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'labels': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TasksFilterForm, self).__init__(*args, **kwargs)
        self.fields['labels'].empty_label = '---------'
