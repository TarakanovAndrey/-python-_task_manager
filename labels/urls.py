from django.urls import path
from . import views


urlpatterns = [
    path('labels/', views.LabelsListView.as_view(), name='labels_list'),
    path('labels/create/', views.LabelCreateView.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', views.LabelUpdateView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label_delete'),
]
