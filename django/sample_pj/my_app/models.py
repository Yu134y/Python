from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)  # カラム定義
    price = models.IntegerField()  # カラム定義
    release_date = models.DateField()  # カラム定義
