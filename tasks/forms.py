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
                    'class': 'form-control',
                    'placeholder': _('Description'),
                    'required': True,
                }
            ),
            'executor': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Executor'),
                    'required': False,
                }
            ),
            'labels': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'placeholder': _('Labels'),
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
                    'placeholder': _('Description'),
                }
            ),
            'executor': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': _('Executor'),
                }
            ),
            'labels': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': _('Labels'),
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TasksFilterForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False
        self.fields['executor'].required = False
        self.fields['labels'].required = False
        self.fields['labels'].empty_label = '---------'
