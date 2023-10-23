from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('users/', views.get_users_list, name='users_list'),
    path('users/create/', views.RegisterUserView.as_view(), name='create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
]
