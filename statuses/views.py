from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from statuses.models import Status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses_list'

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(StatusesListView, self).handle_no_permission()


class StatusCreateView(LoginRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):
        form = forms.CreateStatusForm()
        return render(request, template_name='statuses/status_create.html', context={'form': form})

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(StatusCreateView, self).handle_no_permission()

    def post(self, request, *args, **kwargs):
        form = forms.CreateStatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.save()
            messages.success(request, _('Status successfully created'))
            return redirect('statuses_list')
        return render(request, 'statuses/status_create.html', {'form': form})


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = forms.CreateStatusForm
    success_url = reverse_lazy('statuses_list')

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(StatusUpdateView, self).handle_no_permission()

    def form_valid(self, form):
        messages.success(self.request, _('Status successfully updated'))
        return super(StatusUpdateView, self).form_valid(form)


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = "/login/"
    model = Status
    success_url = reverse_lazy('statuses_list')
    context_object_name = 'status'
    success_message = _('Status successfully deleted')

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(StatusDeleteView, self).handle_no_permission()

    def form_valid(self, form):
        try:
            return super(StatusDeleteView, self).form_valid(form)
        except ProtectedError:
            messages.error(self.request, _('It is not possible to delete the status because it is being used'))
            return redirect('statuses_list')


