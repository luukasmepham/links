from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import random
from .models import Category

def index(request):
    all_categories = Category.objects.count()
    latest_category_1 = Category.objects.get(id=all_categories)
    latest_category_2 = Category.objects.get(id=all_categories-1)
    latest_category_3 = Category.objects.get(id=all_categories-2)

    category_1_word_1 = latest_category_1.word_1
    category_1_word_2 = latest_category_1.word_2
    category_1_word_3 = latest_category_1.word_3
    category_2_word_1 = latest_category_2.word_1
    category_2_word_2 = latest_category_2.word_2
    category_2_word_3 = latest_category_2.word_3
    category_3_word_1 = latest_category_3.word_1
    category_3_word_2 = latest_category_3.word_2
    category_3_word_3 = latest_category_3.word_3

    word_list = []

    word_list.append(latest_category_1.word_1)
    word_list.append(latest_category_1.word_2)
    word_list.append(latest_category_1.word_3)
    word_list.append(latest_category_2.word_1)
    word_list.append(latest_category_2.word_2)
    word_list.append(latest_category_2.word_3)
    word_list.append(latest_category_3.word_1)
    word_list.append(latest_category_3.word_2)
    word_list.append(latest_category_3.word_3)

    random.shuffle(word_list)

    context = {
            "word_list" : word_list,
            "category_1" : latest_category_1.category_text,
            "category_2" : latest_category_2.category_text,
            "category_3" : latest_category_3.category_text,
            "category_1_word_1" : latest_category_1.word_1,
            "category_1_word_2" : latest_category_1.word_2,
            "category_1_word_3" : latest_category_1.word_3,
            "category_2_word_1" : latest_category_2.word_1,
            "category_2_word_2" : latest_category_2.word_2,
            "category_2_word_3" : latest_category_2.word_3,
            "category_3_word_1" : latest_category_3.word_1,
            "category_3_word_2" : latest_category_3.word_2,
            "category_3_word_3" : latest_category_3.word_3,
        }
    return render(request, 'links_app/index.html', context)