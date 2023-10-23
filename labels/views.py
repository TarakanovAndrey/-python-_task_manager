from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from labels.models import Label
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def get_list_labels(request):
    if not request.user.is_authenticated:
        return redirect('login')

    labels_list = Label.objects.all()
    return render(
        request,
        'labels/labels_list.html',
        context={
            'labels_list': labels_list,
        },
    )


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
            messages.success(request, _('OK'))
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
        messages.success(self.request, 'OK')
        return super(LabelUpdateView, self).form_valid(form)


class LabelDeleteView(DeleteView):
    model = Label
    success_url = reverse_lazy('labels_list')
    context_object_name = 'label'

    def form_valid(self, form):
        messages.success(self.request, 'OK')
        return super(LabelDeleteView, self).form_valid(form)
