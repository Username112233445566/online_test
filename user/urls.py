from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserRegisterView.as_view(), name='user'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]