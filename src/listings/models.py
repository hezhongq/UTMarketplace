from users.models import UserExtension
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Table of Categories
# No duplicates
# Contains category name and it's parent category, if it exists.
# Example: You want to filter for all Books. We can select name=Books or parent_category=Books
# Textbook's parent_category is Book
class Category(models.Model):
    name = models.CharField(max_length=64)
    parent_category = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

# A listing has an item name, price, title, description, posted date, modified date, and image
# Also has a reference to a category object which it is affiliated with and the original poster
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


# Bookmark model contains a foreign key to a UserExtension which is the user who created the bookmark
# Additionally has a reference to the listing object which is bookmarked by the user
class Bookmark(models.Model):
    owner = models.ForeignKey(UserExtension, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


