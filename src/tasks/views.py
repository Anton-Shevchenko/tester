from django.shortcuts import render
from django.http import JsonResponse
import os
import importlib
from .models import Test, Task, Job
from myapp.models import User


def representsInt(s):
    try:
        s = int(s)
        return s
    except ValueError:
        return s


def index(request):
    user = User.objects.get(id=request.user.id)

    if user.group_id is not None:
        group_id = user.group_id.id
        tasks = Task.objects.filter(group_id=group_id)
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def task(request, pk):
    user = User.objects.get(id=request.user.id)

    if user.group_id is not None:
        group_id = user.group_id.id
        tasks = Task.objects.filter(group_id=group_id)
    else:
        tasks = Task.objects.all()

    job = Job.objects.filter(user_id=request.user.id, task_id=pk).exists()

    if job:
        job = Job.objects.get(user_id=request.user.id, task_id=pk)

    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/index.html', {'task': task, 'tasks': tasks, "job": job})


def run_cpp(request):
    code = request.POST.get('code')
    text_code = ('#include <boost/python.hpp>\n' +
                 code + '\n' +
                 'BOOST_PYTHON_MODULE(codecpp)\n' +
                 '{\n' +
                 'using namespace boost::python;\n' +
                 'def("greet", greet);\n' +
                 '}')

    f = open("codecpp.cpp", "w+")
    f.write(text_code)
    f.close()

    os.system("gcc -c -fPIC -I/usr/include/boost -I/usr/include/python3.6 codecpp.cpp")
    os.system(
        "gcc codecpp.o -shared -Wl,-soname,codecpp.so -Wl,-rpath,/usr/lib/x86_64-linux-gnu" +
        " -L/usr/lib/x86_64-linux-gnu -lboost_python3 -o codecpp.so")

    import codecpp
    response = codecpp.greet()
    return JsonResponse({"ok": response})


def run_python(request):
    code = request.POST.get('code')
    name = request.POST.get('name')
    task_id = request.POST.get('task_id')
    f = open("codepy.py", "w+")
    f.write(code)
    f.close()
    job = Job()
    job.code = code
    job.user_id = User.objects.get(id=request.user.id)
    job.task_id = Task.objects.get(id=request.POST.get('task_id'))

    try:
        import codepy
        importlib.reload(codepy)
        tests = Test.objects.filter(task_id=task_id)
        for test in tests:
            params = test.params.split(',')
            type_params = []
            for param in params:
                type_params.append(representsInt(param))
            if len(params) == 0:
                response = getattr(codepy, name)()
            elif len(params) == 1:
                response = getattr(codepy, name)(type_params[0])
            elif len(params) == 2:
                response = getattr(codepy, name)(type_params[0], type_params[1])
            elif len(params) == 3:
                response = getattr(codepy, name)(type_params[0], type_params[1], type_params[2])
            elif len(params) == 4:
                response = getattr(codepy, name)(type_params[0], type_params[1], type_params[2], type_params[3])
            elif len(params) == 5:
                response = getattr(codepy, name)(type_params[0], type_params[1], type_params[2],
                                                 type_params[3], type_params[4])
            if str(response) != str(test.result):
                job.status = 2
                job.save()
                return JsonResponse({"error": str(test.params) + ' - has error!'})
            job.status = 5
            job.save()
        return JsonResponse({"ok": response})
    except Exception as e:
        return JsonResponse({"ok": str(e)})
