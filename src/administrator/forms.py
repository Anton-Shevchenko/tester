from django import forms
from tasks.models import Task, Test, Job
from myapp.models import Group
from django.contrib.auth import get_user_model

from blog.models import Post

User = get_user_model()


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'params', 'description', 'language', 'value')


class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('params', 'result', 'task_id')


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('user_id', 'task_id', 'comment', 'status', 'assessment')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'group_id')


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name', )


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)