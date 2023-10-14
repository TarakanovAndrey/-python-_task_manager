from django.urls import path
from users.views import CustomUserFormCreateView, UsersListView, LoginView


urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('create/', CustomUserFormCreateView.as_view(), name='create_user'),
]
