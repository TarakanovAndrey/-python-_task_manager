from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import forms
from django.contrib import messages
from . import models
from django.urls import reverse_lazy


def get_list_tasks(request):
    tasks_list = models.Task.objects.all()
    return render(
        request,
        'tasks/tasks_list.html',
        {'tasks_list': tasks_list}
    )


def get_task_info(request, pk):
    task = models.Task.objects.get(pk=pk)
    task_datas = {
        'task_pk': task.pk,
        'task_name': task.task_name,
        'task_description': task.description,
        'task_author': task.author,
        'task_executor': task.executor,
        'task_status': task.status,
        'task_created': task.created_at,
        'task_labels': task.labels.all(),
    }

    return render(request,
                  'tasks/task_info.html',
                  {'task_datas': task_datas})


class TaskCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = forms.TaskCreateForm
        return render(request, 'tasks/task_create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = forms.TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = self.request.user
            task.save()
            messages.success(request, 'OKKK')
            return redirect('tasks_list')
        return render(request, 'tasks/task_create.html', {'form': form})


class TaskUpdateView(UpdateView):
    model = models.Task
    form_class = forms.TaskCreateForm
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        messages.success(self.request, 'OK')
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(DeleteView):
    model = models.Task
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        messages.success(self.request, 'OK')
        return super(TaskDeleteView, self).form_valid(form)