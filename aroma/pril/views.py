from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import Product, Planogram
from .forms import ProductForm, PlanogramForm
from datetime import datetime, timedelta
from django.db.models import Q


@login_required
def index(request):
    if request.POST:
        delete = request.POST.getlist('prod[]')
        for i in delete:
            x = Product.objects.get(pk=i)
            x.delete()
            redirect('pril:index')
    today = datetime.today()
    date_plus_5_days = today + timedelta(days=5)
    pr_fresh = Product.objects.filter(date_snat__gte=date_plus_5_days.date())
    poison = Product.objects.filter(date_snat__lt=datetime.today())
    pr_30 = Product.objects.filter(Q(date_snat__lt=date_plus_5_days.date()) & Q(date_snat__gt=datetime.today()))
    fresh = serializers.serialize('python', pr_fresh)
    prod_30 = serializers.serialize('python', pr_30)
    context = {
        'fresh': fresh,
        'poison': poison,
        'prod_30': prod_30,
    }
    return render(request, 'pril/index.html', context)


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
