from django.db import models
from myapp.models import Group
from myapp.models import User


class Task(models.Model):
    name = models.CharField(max_length=255)
    params = models.CharField(max_length=255)
    description = models.TextField()
    language = models.CharField(max_length=255)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Test(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    params = models.CharField(max_length=255)
    result = models.CharField(max_length=255)

    def __str__(self):
        return self.id


class Job(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    code = models.TextField(null=True, blank=True)
    status = models.IntegerField()
    assessment = models.IntegerField(null=True)
    comment = models.TextField()
