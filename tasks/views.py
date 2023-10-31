from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import forms
from django.contrib import messages
from . import models
from django.urls import reverse_lazy
from tasks.support_functions import get_filtered_tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _


class TasksListView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(TasksListView, self).handle_no_permission()

    def get(self, request, *args, **kwargs):

        form = forms.TasksFilterForm(request.GET)

        request_parameters = request.GET
        user = request.user
        if any(request_parameters.values()) is False:
            form = forms.TasksFilterForm()
            tasks_list = models.Task.objects.all()
            return render(request, 'tasks/tasks_list.html', {
                'form': form,
                'tasks_list': tasks_list
            })

        else:
            tasks_list = get_filtered_tasks(request_parameters, user)

            return render(request, 'tasks/tasks_list.html', {
                'form': form,
                'tasks_list': tasks_list
            })


class TaskInfoView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/task_info.html'
    model = models.Task
    context_object_name = 'task'

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(TaskInfoView, self).handle_no_permission()


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'tasks/task_create.html'
    form_class = forms.TaskCreateForm
    success_url = reverse_lazy('tasks_list')
    success_message = _('The task was successfully created')

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(TaskCreateView, self).handle_no_permission()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    form_class = forms.TaskCreateForm
    success_url = reverse_lazy('tasks_list')

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(TaskUpdateView, self).handle_no_permission()

    def form_valid(self, form):
        messages.success(self.request, _('The task has been successfully changed'))
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task
    success_url = reverse_lazy('tasks_list')

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(TaskDeleteView, self).handle_no_permission()

    def form_valid(self, form):
        if self.object.author != self.request.user:
            messages.error(self.request, _("A task can only be deleted by its author"))
            return redirect('tasks_list')

        messages.success(self.request, _('The task was successfully deleted'))
        return super(TaskDeleteView, self).form_valid(form)
