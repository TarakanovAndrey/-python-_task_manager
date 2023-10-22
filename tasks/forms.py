from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
import django_filters


class TaskCreateForm(ModelForm):

    class Meta:
        model = models.Task
        fields = ['task_name', 'description', 'status', 'executor', 'labels']
        labels = {
            'task_name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
        widgets = {
            'task_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name')
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Description')
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Description'),
                }
            ),
            'executor': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Executor'),
                }
            ),
            'labels': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'placeholder': _('Labels'),
                }
            )
        }


class TasksFilterForm(ModelForm):


    class Meta:
        model = models.Task
        fields = ['status', 'executor', 'labels',]
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


