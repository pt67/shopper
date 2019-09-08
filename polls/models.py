import datetime
from django.db import models
from django.utils import timezone

class Product(models.Model):
    product_text = models.CharField(max_length=200, default='null')
    pub_date = models.DateTimeField('date Published', default='null')
    def __str__(self):
        return self.product_text

class Choice(models.Model):
    question = models.ForeignKey(Product, on_delete=models.CASCADE, default='null')
    choice_text = models.CharField(max_length=200, default='null')
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Food(models.Model):
    food =  models.CharField(max_length=200, default='null')


