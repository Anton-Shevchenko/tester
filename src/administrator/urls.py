from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='control_index'),
    path('users/', views.users, name='control_users'),
    path('users/create/', views.users_create, name='control_users_create'),
    path('ajax/users/', views.ajax_users, name='control_ajax_users'),
    path('jobs/', views.jobs, name='control_jobs'),
    path('jobs/<int:pk>/view/', views.jobs_view, name='control_jobs_view'),
    path('jobs/<int:pk>/update/', views.jobs_update, name='control_jobs_update'),
    path('tasks/', views.tasks, name='control_tasks'),
    path('tasks/create/', views.tasks_create, name='control_tasks_create'),
    path('tasks/<int:pk>/update/', views.tasks_update, name='control_tasks_update'),
    path('tests/<int:pk>/', views.tests_view, name='control_tests_ajax'),
    path('ajax/tests/<int:pk>/', views.ajax_tests, name='control_tests_view'),
    path('tests/create/', views.tests_create, name='control_tests_create'),
    path('ajax/tasks/', views.ajax_tasks, name='control_ajax_tasks'),
    path('groups/create/', views.ajax_groups, name='control_ajax_groups'),
    path('blog/posts/', views.posts_list, name='control_posts_list'),
    path('blog/posts/create/', views.posts_create, name='control_posts_create'),
    path('blog/posts/ajax/', views.posts_list_ajax, name='control_posts_list_ajax'),
]