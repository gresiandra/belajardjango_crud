from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import loginForm

def index(request):

    context = {
        'heading':'Halaman Index'
    }

    return render(request, 'index.html', context)

def loginView(request):

    context = {
        'heading':'Halaman Login',
        'formLogin':loginForm
    }

    if request.method == 'POST':

        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('crud:index')
    
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('crud:index')
        else:
            return render(request, 'login.html', context)