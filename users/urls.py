from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('create/', views.RegisterUserView.as_view(), name='create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
]
