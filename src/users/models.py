from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class UserExtension(models.Model):
    # TODO set global static flags
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    # TODO add image file and ratings in next sprint
    
    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.user.__str__()

class Listing(models.Model):
    item_name = models.CharField(max_length=25)
    user_email = models.EmailField(max_length=254)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    title = models.TextField(max_length=64)
    description = models.TextField(max_length=61000)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    post_user = models.ForeignKey(on_delete=CASCADE)
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

class Bookmark(models.Model):
    def __init__(self):
        self.



 


class Category(models.Model):
    name = models.CharField(max_length=64)
    parent_category = models.CharField(max_length=64)

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_extension(sender, instance, created **kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()

    