from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.detail, name='detail'),
    path('<int:category_id>/word_options/', views.results, name='results'),
]