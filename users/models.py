from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import FloatField
from django_countries.fields import CountryField


# Create your models here.


class UpdateInfo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    profile_pic = models.ImageField()
    designation = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, null=True, blank=False)
    username = models.CharField(
        max_length=255, null=True, blank=False, unique=True)
    password = models.CharField(max_length=255, null=True, blank=False)
    country = CountryField(blank=True, null=True,
                           blank_label='SELECT COUNTRIES')
    phone = models.CharField(max_length=255, blank=True, null=True)
    about_me = RichTextField(null=True, blank=True)
    followers = models.FloatField(max_length=255, blank=True, null=True)
    following = models.FloatField(max_length=255, blank=True, null=True)
    portfolio = models.FloatField(max_length=255, blank=True, null=True)
    views = models.FloatField(max_length=255, blank=True, null=True)
    agree = models.BooleanField(blank=False, null=True)

    def __str__(self):
        return self.name


class SocialSettings(models.Model):
    user = models.ForeignKey(
        UpdateInfo, on_delete=models.SET_NULL, null=True, default=1)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linked_In = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    google_Analytics = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.facebook
