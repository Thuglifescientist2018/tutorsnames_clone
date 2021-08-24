from django.db import models
from django.contrib.auth.models import (AbstractUser)


from django_countries.fields import CountryField
from ckeditor.fields import RichTextField


# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=False, null=True,
                              max_length=255, unique=True)
    username = models.CharField(
        blank=False, null=True, unique=True, max_length=255)
    select_country = CountryField(
        blank_label="Select Countries", default="Select Countries")
    designation = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    about_me = RichTextField(blank=True, null=True)
    change_avatar = models.ImageField(
        default="", upload_to="images/", blank=True, null=True)
    follow = models.BooleanField(default=False, blank=True, null=True)
    # urlfield so that we can make it customizable in cms
    view_profile = models.URLField(blank=True, null=True)
    followers = models.FloatField(blank=True, null=True)
    following = models.FloatField(blank=True, null=True)
    portfolio = models.IntegerField(blank=True, null=True)
    views = models.FloatField(blank=True, null=True)
