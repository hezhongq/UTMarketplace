from django.db import models
from django.utils import timezone
# Create your models here.


class User(models):
    # TODO set global static flags

    name = models.CharField(max_length=50)  
    email = models.EmailField(max_length=254)    # TODO validate emails, emails should be unique ie no two users share the same email
    password = models.CharField(max_length=16)  # TODO validate password, passwords need to be strong
    bookmarks = models.ForeignKey('Listing', on_delete=models.CASCADE, blank=True)
    listings = models.ForeignKey('Listing', on_delete=SET_NULL, blank=True)   # If user deletes account, we shouldnt delete their listings

    def __str__(self):
        return self.name

class Listing(models.Model):
    item_name = models.CharField(max_length=25)
    user_email = models.EmailField(max_length=254)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    title = models.TextField(max_length=64)
    description = models.TextField(max_length=61000)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # Maybe we change to on_delete to set "uncategorized" instead?

    # TODO add edit history

    post_date = models.DateTimeField(editable=False) # auto_now and autop_now_add will be depreciated
    last_modified_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        """Update timestamps"""
        if not self.id:
            self.post_date = timezone.now()
        self.last_modified_date = timezone.noew()

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name


class Category(models.Model):
    name = models.CharField(max_length=64)
    parent_category = models.CharField(max_length=64)

    def __str__(self):
        return self.name

