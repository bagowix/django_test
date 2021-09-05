from django.shortcuts import render, redirect
from .models import DataBase
from .forms import DataBaseForm


def database_home(request):
    database = DataBase.objects.order_by('-date')
    return render(request, "database/db_home.html", {'database': database})


def add_unit(request):
    error = ''
    if request.method == "POST":
        form = DataBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = DataBaseForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, "database/add_unit.html", data)