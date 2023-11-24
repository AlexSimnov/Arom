from django.urls import path
from . import views

app_name = 'pril'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.Product_post, name='add_new'),
    path('planogram/', views.planogram, name='planogram_list'),
    path('planogram/edit/', views.planogram_edit, name='planogram_edit'),
]
