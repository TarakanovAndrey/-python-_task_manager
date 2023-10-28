from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.get_tasks_list, name='tasks_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    # path('tasks/<int:pk>/', views.get_task_info, name='task_info'),
    path('tasks/<int:pk>/', views.TaskInfoView.as_view(), name='task_info'),
]
