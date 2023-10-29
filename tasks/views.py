from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import forms
from django.contrib import messages
from . import models
from django.urls import reverse_lazy
from tasks.support_functions import get_filtered_tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


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


class TaskInfoView(LoginRequiredMixin, ListView):
    # context_object_name = 'tasks'

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(TaskInfoView, self).handle_no_permission()

    def get(self, request, *args, **kwargs):
        task = models.Task.objects.get(pk=kwargs['pk'])
        return render(request,
                      'tasks/task_info.html',
                      {'task': task}
                      )


class TaskCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = forms.TaskCreateForm
        return render(request, 'tasks/task_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)

            task.author = self.request.user
            task.author_fullname = f"{self.request.user.first_name} {self.request.user.last_name}"

            executor = User.objects.get(id=task.executor.id)
            task.executor_fullname = f"{executor.first_name} {executor.last_name}"

            task.save()
            messages.success(request, _('The task was successfully created'))
            return redirect('tasks_list')
        return render(request, 'tasks/task_create.html', {'form': form})


class TaskUpdateView(UpdateView):
    model = models.Task
    form_class = forms.TaskCreateForm
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        messages.success(self.request, _('The task has been successfully changed'))
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(DeleteView):
    model = models.Task
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        messages.success(self.request, _('The task was successfully deleted'))
        return super(TaskDeleteView, self).form_valid(form)
