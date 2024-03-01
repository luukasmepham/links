from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_results/', views.check_results, name='check_results'),
]