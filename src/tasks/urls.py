from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.task, name='task'),
    path('boost/run_cpp/', views.run_cpp, name='run_cpp'),
    path('run_python/', views.run_python, name='run_python')
]