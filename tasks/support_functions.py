from . import models


def is_true(pair):
    key, value = pair
    if value:
        return True


def get_filtered_tasks(request_parameters, user):
    filtered_request = dict(filter(is_true, request_parameters.items()))
    if 'self_tasks' in filtered_request:
        filtered_request.pop('self_tasks')
        filtered_request['author'] = user

    tasks_list = models.Task.objects
    for key, value in filtered_request.items():
        if tasks_list:
            tasks_list = tasks_list.filter(**{key: value})

    return tasks_list
