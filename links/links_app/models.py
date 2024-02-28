from django.db import models


class Category(models.Model):
    category_text = models.CharField(max_length=50)
    def __str__(self):
        return self.category_text


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=20)
    def __str__(self):
        return self.word_text
