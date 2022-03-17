from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        if extra_fields.get("is_active") is not True:
            raise ValueError(
                "Superuser must have is_active=True."
            )

        return self._create_user(email, password, **extra_fields)


class UserExtension(AbstractUser):
    # TODO set global static flags
    # TODO add image file and ratings in next sprint
    # avatar = ProcessedImageField(upload_to='avatar',default='avatar/default.png', verbose_name='image')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, blank=False)
    is_active = models.BooleanField(_('active'), default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Bookmark table
# An entry contains a user and a listing.
# No duplicate entries allowed
# Example for get table of all listings of a user: SELECT listing FROM Bookmark WHERE user=user;
# class Bookmark(models.Model):
#     owner = models.ForeignKey(UserExtension, on_delete=models.CASCADE)
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="verified_code")
    email = models.EmailField(max_length=50, verbose_name="email")
    send_type = models.CharField(verbose_name="type", max_length=10,
                                 choices=(("register", "register"), ("forget", "forget")))
    send_time = models.DateTimeField(verbose_name="send_time", default=timezone.now)

    class Meta:
        verbose_name = "email_verified_code"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

