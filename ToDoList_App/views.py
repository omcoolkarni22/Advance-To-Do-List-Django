from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from .models import Tasks


@user_passes_test(lambda user: not user.username, login_url='login', redirect_field_name=None)
def index(request):
    return render(request, 'index.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['form-username']
        password = request.POST['form-password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            todo = Tasks.objects.filter(email=username)
            todo_fi = todo.filter(is_InProgress=True)
            try:
                todo_fi_ini = todo_fi.filter(is_archive=False)
                todo_fin = todo_fi_ini.filter(is_completed=False)
                context = {
                    "todos": todo_fin
                }
                return render(request, 'tasks_in.html', context)
            except:
                context = {
                    "todos": todo_fi
                }
                return render(request, 'tasks_in.html', context)
        else:
            messages.error(request, " Invalid Log-in Request or User won't exist ")
            return redirect('/')
    else:
        todo = Tasks.objects.filter(email=request.user.username)
        todo_fi = todo.filter(is_InProgress=True)
        try:
            todo_fi_ini = todo_fi.filter(is_archive=False)
            todo_fin = todo_fi_ini.filter(is_completed=False)
            context = {
                "todos": todo_fin
            }
            return render(request, 'tasks_in.html', context)
        except:
            context = {
                "todos": todo_fi
            }
            return render(request, 'tasks_in.html', context)


def Register(request):
    if request.method == 'POST':
        uname = request.POST['form-uname']
        password = request.POST['form-pass']
        cnfrm_pass = request.POST['form-confirm-password']

        if cnfrm_pass == password:
            try:
                user = User.objects.get(username=uname)
                messages.error(request, 'Email is registered with other Account')
                return render(request, 'index.html')

            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=uname,
                    password=cnfrm_pass
                )
                user.save()
                user_4log = authenticate(request, username=uname, password=cnfrm_pass)
                login(request, user_4log)
                return redirect('login')
        else:
            messages.error(request, 'Password & Confirm Password won"t Match')
            return redirect('/')


def Logout(request):
    logout(request)
    messages.success(request, 'Logged out ! Successfully')
    return redirect('/')


def Archive(request):
    arch = Tasks.objects.filter(email=request.user.username)
    arch_fi = arch.filter(is_archive=True)
    context = {
        "archives": arch_fi
    }
    return render(request, 'tasks_in.html', context)


def add_tasks(request):
    if request.method == 'POST':
        task = request.POST['task']
        deadline = request.POST['deadline']
        type = request.POST['t_bar']
        # print(request.user.username)
        tasks_a = Tasks()
        tasks_a.Task = task
        tasks_a.end_date = deadline
        tasks_a.email = request.user.username
        tasks_a.type = type
        tasks_a.save()
        messages.success(request, 'Success ! Task has been Added')
        return redirect('login')


def Back(request):
    return redirect('login')


def Update(request, id):
    if request.method == 'POST':
        act = request.POST['bar']
        # print(act)
        uni = Tasks.objects.get(pk=id)
        if act == 'in_progress':
            uni.is_InProgress = True
        elif act == 'completed':
            uni.is_completed = True
        elif act == 'archive':
            uni.is_archive = True
            uni.is_completed = True
        uni.save()
        messages.success(request, 'Success ! Changes Saved')
        return redirect('login')

