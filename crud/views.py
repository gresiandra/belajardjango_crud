from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import smartphoneModel
from .forms import smartphoneForm

# Create your views here.

def index(request):

    smartphones = smartphoneModel.objects.all()

    context = {
        'heading':'Crud Home',
        'smartphones':smartphones,
    }

    return render(request, 'crud/index.html', context)


def create(request):

    form = smartphoneForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('crud:index')

    context = {
        'heading':'Crud Create',
        'form':form
    }

    return render(request, 'crud/create.html', context)


def delete(request, delete_id):

    smartphoneModel.objects.filter(id=delete_id).delete()

    return redirect('crud:index')


def update(request, update_id):

    smartphoneUpdate = smartphoneModel.objects.get(id=update_id)

    data = {
        'Nama':smartphoneUpdate.Nama,
        'Brand':smartphoneUpdate.Brand,
        'TahunRilis':smartphoneUpdate.TahunRilis
    }

    formUpdate = smartphoneForm(request.POST or None, initial=data, instance=smartphoneUpdate)

    if request.method == 'POST':
        if formUpdate.is_valid():
            formUpdate.save()
            return redirect('crud:index')

    context = {
        'heading':'Crud Update',
        'form':formUpdate
    }

    return render(request, 'crud/create.html', context)

@login_required
def logoutView(request):

    if request.method == 'POST':

        if request.POST['logout'] == 'Submit Query':
            logout(request)
            return redirect('login')

    print(request.POST)
    context = {

    }

    return render(request, 'crud/logout.html', context)
