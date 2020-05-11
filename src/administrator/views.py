from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone
from tasks.models import Task, Job
from django.http import JsonResponse, HttpResponseNotFound
from .forms import TaskForm, UserForm, GroupForm, TestForm, JobForm, PostForm
from myapp.forms import CustomUserCreationForm
from myapp.models import Group
from django.core import serializers
from blog.models import Post

User = get_user_model()


def index(request):
    return render(request, 'administrator/index.html', {})


def users(request):
    return render(request, 'administrator/users/index.html', {})


def users_create(request):
    if request.method == "POST":
        user = User.objects.create_user(
            request.POST.get('email'),
            first_name=request.POST.get('first_name'),
            password=request.POST.get('password'),
            group_id=Group.objects.get(pk=request.POST.get('group_id')))
        if user:
            return JsonResponse({"data": "ok"})
        return JsonResponse({"data": "error"})
    else:
        group_form = GroupForm()
        form = CustomUserCreationForm()

    return render(request, 'administrator/users/create.html', {'form': form, "group_form": group_form})


def ajax_users(request):
    data_users = User.objects.all().values()

    return JsonResponse({"data": list(data_users)})


def ajax_groups(request):
    form = GroupForm(request.POST)
    if form.is_valid():
        group = form.save()

    return JsonResponse({"data": group})


def tasks(request):
    return render(request, 'administrator/tasks/index.html', {})


def jobs(request):
    data_jobs = Job.objects.all().values()
    if request.method == "POST":
        return JsonResponse({"data": list(data_jobs)})

    return render(request, 'administrator/jobs/index.html', {})


def jobs_view(request, pk):
    job = Job.objects.get(pk=pk)

    return render(request, 'administrator/jobs/view.html', {'job': job})


def jobs_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job.save()
            return redirect('control_jobs_update', pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'administrator/jobs/update.html', {'form': form})


def tasks_create(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return JsonResponse({"data": "ok"})
    else:
        form_task = TaskForm()
        form_test = TestForm()

    return render(request, 'administrator/tasks/create.html', {'form_task': form_task, 'form_test': form_test})


def tests_create(request):

    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.save()
            serialized_test = serializers.serialize('json', [ test, ])
            return JsonResponse({"data": serialized_test})

    return HttpResponseNotFound('Test not found')


def ajax_tasks(request):
    data_tasks = Task.objects.all().values()

    return JsonResponse({"data": list(data_tasks)})


def posts_list(request):
    return render(request, 'administrator/blog/index.html', {})


def posts_create(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
          
            return JsonResponse({"data": "ok"})
    else:
        form = PostForm()

    return render(request, 'administrator/blog/create.html', {'form': form})


def posts_list_ajax(request):
    data_tasks = Post.objects.all().values()

    return JsonResponse({"data": list(data_tasks)})