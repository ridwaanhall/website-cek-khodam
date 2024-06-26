from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cek-khodam/', views.cek_khodam, name='cek-khodam'),
]
