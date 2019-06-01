from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'contact/index.html')

def userlogin(request):
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('/')
        else:
            return HttpResponse("<h2> There seems to be problem with adding data. Please Try Again</h1>")
    else:
        form = LoginForm()
    return render(request, 'contact/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return HttpResponse("<h2> There seems to be problem with adding data. Please Try Again</h1>")
    else:
        form = RegisterForm()
    return render(request, 'contact/register.html', {'form': form})

def userlogout(request):
    logout(request)
    return redirect('/')