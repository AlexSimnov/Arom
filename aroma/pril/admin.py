from django.contrib import admin
from .models import Product, Planogram


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Planogram)
class PlanogramAdmin(admin.ModelAdmin):
    list_display = ('date_add',)
