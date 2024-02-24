from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop


def laptop_create_view(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(form.POST)
        if form.is_valid():
            form.save()
            return redirect("retrive_url")
    template_name = 'crud_app/home.html'
    context = {'form': form}
    return render(request, template_name, context)


def laptop_retrive_view(request):
    objs = Laptop.objects.all()
    template_name = 'crud_app/laptop_list.html'
    context = {'data': objs}
    return render(request, template_name, context)


def laptop_update_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(form.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("retrive_url")
    template_name = 'crud_app/home.html'
    context = {'form': form}
    return render(request, template_name, context)


def laptop_delete_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    template_name = 'crud_app/laptop_list.html'
    obj.delete()
    return redirect('retrive_url')
    template_name = 'crud_app/delete.html'
    context = {'obj': obj}
    return render(request, template_name, context)

