from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from statuses.models import Status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def get_list_statuses(request):
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
            status = form.save()
            status.save()
            messages.success(request, _('OK'))
            return redirect('statuses_list')
        return render(request, 'statuses/status_create.html', {'form': form})


class StatusUpdateView(UpdateView):
    model = Status
    form_class = forms.CreateStatusForm
    success_url = reverse_lazy('statuses_list')

    def form_valid(self, form):
        messages.success(self.request, 'OK')
        return super(StatusUpdateView, self).form_valid(form)


class StatusDeleteView(DeleteView):
    model = Status
    success_url = reverse_lazy('statuses_list')
    context_object_name = 'status'

    def form_valid(self, form):
        messages.success(self.request, 'OK')
        return super(StatusDeleteView, self).form_valid(form)

