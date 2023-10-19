from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('users/', views.ListUsersView.as_view(), name='users_list'),
    path('users/create/', views.RegisterUser.as_view(), name='create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
]
