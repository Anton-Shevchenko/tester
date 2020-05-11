from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.users_logout, name='users_logout'),
    path('login/', views.users_login, name='users_login'),
]