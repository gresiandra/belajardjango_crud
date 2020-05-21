from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):

    context = {
        'heading':'Halaman Index'
    }

    return render(request, 'index.html', context)

def loginView(request):

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('crud:index')

    context = {
        'heading':'Halaman Login'
    }

    return render(request, 'login.html', context)