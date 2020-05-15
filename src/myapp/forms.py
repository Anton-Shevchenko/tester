from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Group


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'group_id')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'group_id')
