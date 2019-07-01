from django.db import models

class ShopItem(models.Model):

    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, unique=True)
