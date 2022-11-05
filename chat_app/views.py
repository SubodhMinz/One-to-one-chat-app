from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def home(request, id=None):
    users = User.objects.exclude(username=request.user)
    user = ''

    try:
        user = User.objects.get(id=id)
    except Exception as e:
        pass

    context = {
        'users':users,
        'user':user,
        'id':id
    }
    return render(request, 'chat_app/index.html', context)

def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return redirect('/login/')
    return render(request, 'chat_app/login.html', {'form':form})


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered!')
    form = UserCreationForm()
    return render(request, 'chat_app/signup.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('/login/')