from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from labels.models import Label
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels_list'

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(LabelsListView, self).handle_no_permission()


class LabelCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = forms.CreateLabelForm()
        return render(
            request,
            template_name='labels/label_create.html',
            context={'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.CreateLabelForm(request.POST)
        if form.is_valid():
            label = form.save()
            label.save()
            messages.success(request, _('The label was created successfully'))
            return redirect('labels_list')
        return render(
            request,
            'labels/label_create.html',
            {'form': form})


class LabelUpdateView(UpdateView):
    model = Label
    form_class = forms.CreateLabelForm
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        messages.success(self.request, _('Label changed successfully'))
        return super(LabelUpdateView, self).form_valid(form)


class LabelDeleteView(DeleteView):
    model = Label
    success_url = reverse_lazy('labels_list')
    context_object_name = 'label'

    def form_valid(self, form):
        messages.success(self.request, _('The label was successfully deleted'))
        return super(LabelDeleteView, self).form_valid(form)
