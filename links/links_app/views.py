from django.shortcuts import render
from django.http import HttpResponse

from .models import Category

def index(request):
    latest_category_list = Category.objects.all()
    context = {'latest_category_list': latest_category_list}
    return render(request, 'links_app/index.html', context)

def detail(request, category_id):
    return HttpResponse("You're looking at category %s." % category_id)

def results(request, category_id):
    response = "You're looking at the word options for category %s."
    return HttpResponse(response % category_id)