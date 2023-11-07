from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import Product, Planogram
from .forms import ProductForm, PlanogramForm
import datetime as dt


@login_required
def index(request):
    product = Product.objects.filter(date_snat__gte=dt.date.today())
    data = serializers.serialize('python', product)
    context = {
        'data': data,
    }
    return render(request, 'pril/index.html', context)


@login_required
def poison(request):
    if request.POST:
        delete = request.POST.getlist('prod[]')
        for i in delete:
            x = Product.objects.get(pk=i)
            x.delete()
            redirect('pril:poison')
    products = Product.objects.filter(date_snat__lt=dt.date.today())
    context = {
        'products': products,
    }
    return render(request, 'pril/poison_index.html', context)


@login_required
def Product_post(request):
    form = ProductForm(request.POST)
    if 'save' in request.POST:
        if form.is_valid():
            products = form.save()
            products.save()
            return redirect('pril:index')
    if 'add' in request.POST:
        if form.is_valid():
            products = form.save()
            products.save()
            return redirect('pril:add_new')
    context = {
        'form': form,
    }
    return render(request, 'pril/product_post.html', context)


def planogram(request):
    planogram = Planogram.objects.first()
    context = {
        'planogram': planogram,
    }
    return render(request, 'pril/planogram.html', context)


def planogram_edit(request):
    planogram = get_object_or_404(Planogram, id=6)
    if request.method == 'POST':
        form = PlanogramForm(request.POST, request.FILES, instance=planogram)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.image = request.POST.get('image')
            plan.save()
            return redirect('pril:planogram_list')
    else:
        form = PlanogramForm(instance=planogram)

    context = {
        'form': form,
    }
    return render(request, 'pril/planogram_edit.html', context)


# настроить на автодобав дату
