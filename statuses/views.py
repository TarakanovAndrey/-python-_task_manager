from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from statuses.models import Status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin


def get_list_statuses(request):
    if not request.user.is_authenticated:
        return redirect('login')

    statuses_list = Status.objects.all()
    return render(
        request,
        'statuses/statuses_list.html',
        context={
            'statuses_list': statuses_list,
        },
    )


class StatusCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = forms.CreateStatusForm()
        return render(request, template_name='statuses/status_create.html', context={'form': form})

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


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Status
    success_url = reverse_lazy('statuses_list')
    context_object_name = 'status'

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(StatusDeleteView, self).handle_no_permission()

    def form_valid(self, form):
        try:
            status_delete = super(StatusDeleteView, self).form_valid(form)
            messages.success(self.request, _('Status successfully deleted'))
            return status_delete
        except ProtectedError:
            messages.error(self.request, _('It is not possible to delete the status because it is being used'))
            return redirect('statuses_list')


