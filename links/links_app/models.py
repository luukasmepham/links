from django.db import models


class Category(models.Model):
    category_text = models.CharField(max_length=50)
    word_1 = models.CharField(max_length=20, default='UNDEFINED')
    word_2 = models.CharField(max_length=20,default='UNDEFINED')
    word_3 = models.CharField(max_length=20, default='UNDEFINED')
    def __str__(self):
        return self.category_text
