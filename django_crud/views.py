from django.shortcuts import render

def index(request):

    context = {
        'heading':'Halaman Index'
    }

    return render(request, 'index.html', context)