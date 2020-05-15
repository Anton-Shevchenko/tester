from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import redirect
from myapp.models import User


def users_logout(request):
    logout(request)

    return redirect('/')


def users_login(request):

    user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))

    if user is not None:
        if user.is_active:
            login(request, user)

        return JsonResponse({"data": 'ok'})
    return HttpResponseNotFound('User not found')