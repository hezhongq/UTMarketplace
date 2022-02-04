from django.db import models
# Create your models here.


class Listing(models.Model):
    item_name = models.CharField(max_length=25)
    user_email = models.EmailField(max_length=254)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    title = models.TextField(max_length=64)
    description = models.TextField(max_length=61000)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # Maybe we change to on_delete to set "uncategorized" instead?

    def __str__(self):
        return self.item_name


class Category(models.Model):
    name = models.CharField(max_length=64)
    parent_category = models.CharField(max_length=64)

    def __str__(self):
        return self.name

