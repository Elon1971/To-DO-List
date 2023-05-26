from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import to_do_Form
from .models import to_do_list


def home(request):
    return HttpResponse(f'<body style="background-color:blue"><div style="text-align:center;'
                        f'color:red;'
                        f'padding-top: 40vh;'
                        f'margin: 0;'
                        f' "><h1>To-Do List</h1></div></body>')


def emp(request):
    if request.method == "POST":
        form = to_do_Form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = to_do_Form()
    return render(request, 'index.html', {'form': form})


def show(request):
    employees = to_do_list.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = to_do_list.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = to_do_list.objects.get(id=id)
    form = to_do_Form(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = to_do_list.objects.get(id=id)
    employee.delete()
    return redirect("/show")
