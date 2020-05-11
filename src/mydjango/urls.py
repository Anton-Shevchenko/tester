from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('tasks/', include('tasks.urls')),
    path('users/', include('myapp.urls')),
    path('administrator/', include('administrator.urls')),
    path('users/', include('django.contrib.auth.urls')),
]

