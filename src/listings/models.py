from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.
class Listing(models.Model):
    item_name = models.CharField()
    price = models.FloatField()
    listing_title = models.CharField()
    description = models.CharField()
    category = models.CharField()
    post_date = models.DateField(auto_now_add=True) # When a listing is created, date will be assigned automatically
    last_modified_date = models.DateField(auto_now=True) # When listing is modified, date will be updated automatically

    original_poster = models.ForeignKey(to=User, on_delete=CASCADE)

    def __str__(self) -> str:
        return "{0} -- {1} @ {2} created on {3}".format(self.item_name, self.category, self.price, self.post_date)

