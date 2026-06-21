from django.urls import path
from .views import (
    RegisterView,
    ProfileView,
    UserListView,
    ForgotPasswordView,
    ResetPasswordView,
    AdminStatsView
)

urlpatterns = [
     path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='users'),
    path(
        'forgot-password/',
        ForgotPasswordView.as_view(),
        name='forgot-password'
    ),

    path(
        'reset-password/',
        ResetPasswordView.as_view(),
        name='reset-password'
    ),
    path('admin-stats/', AdminStatsView.as_view(), name='admin-stats'),
]