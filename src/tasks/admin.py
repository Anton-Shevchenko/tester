from django.contrib import admin
from .models import Test, Task, Job


admin.site.register(Task)
admin.site.register(Test)
admin.site.register(Job)
