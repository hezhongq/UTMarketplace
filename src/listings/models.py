from users.models import Category, UserExtension
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


# Create your models here.
class Listing(models.Model):
    item_name = models.CharField(max_length=150)
    price = models.FloatField()
    listing_title = models.CharField(max_length=150)
    description = models.CharField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(auto_now_add=True) # When a listing is created, date will be assigned automatically
    last_modified_date = models.DateField(auto_now=True) # When listing is modified, date will be updated automatically
    image = models.ImageField(upload_to='')

    original_poster = models.ForeignKey(to=UserExtension, on_delete=CASCADE)

    def __str__(self) -> str:
        return "{0} -- {1} @ {2} created on {3}".format(self.item_name, self.category, self.price, self.post_date)


class Bookmark(models.Model):
    owner = models.ForeignKey(UserExtension, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
