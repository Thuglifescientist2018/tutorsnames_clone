from django.db import models

# Create your models here.


class MonthlyStudent(models.Model):
    price = models.FloatField(default=0)
    follow_or_unfollow = models.BooleanField(default=True)
    contact = models.BooleanField(default=False)
    appointment = models.BooleanField(default=True)
    blogs = models.BooleanField(default=False)
    portfolio = models.BooleanField(default=False)
    skill = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    experience = models.BooleanField(default=False)
    testimonials = models.BooleanField(default=True)


class MonthlyTutor(models.Model):
    price = models.FloatField(default=0)
    follow_or_unfollow = models.BooleanField(default=True)
    contact = models.BooleanField(default=True)
    appointment = models.BooleanField(default=True)
    blogs = models.BooleanField(default=False)
    portfolio = models.BooleanField(default=False)
    skill = models.BooleanField(default=True)
    service = models.BooleanField(default=True)
    experience = models.BooleanField(default=False)
    testimonials = models.BooleanField(default=True)


class MonthlyPro(models.Model):
    price = models.FloatField(default=2)
    follow_or_unfollow = models.BooleanField(default=True)
    contact = models.BooleanField(default=True)
    appointment = models.BooleanField(default=True)
    blogs = models.BooleanField(default=True)
    portfolio = models.BooleanField(default=True)
    skill = models.BooleanField(default=True)
    service = models.BooleanField(default=True)
    experience = models.BooleanField(default=True)
    testimonials = models.BooleanField(default=True)


class YearlyStudent(models.Model):
    price = models.FloatField(default=0)
    follow_or_unfollow = models.BooleanField(default=True)
    contact = models.BooleanField(default=False)
    appointment = models.BooleanField(default=True)
    blogs = models.BooleanField(default=False)
    portfolio = models.BooleanField(default=False)
    skill = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    experience = models.BooleanField(default=False)
    testimonials = models.BooleanField(default=True)


class YearlyTutor(models.Model):
    price = models.FloatField(default=0)
    follow_or_unfollow = models.BooleanField(default=True)
    contact = models.BooleanField(default=True)
    appointment = models.BooleanField(default=True)
    blogs = models.BooleanField(default=False)
    portfolio = models.BooleanField(default=False)
    skill = models.BooleanField(default=True)
    service = models.BooleanField(default=True)
    experience = models.BooleanField(default=False)
    testimonials = models.BooleanField(default=True)


class YearlyPro(models.Model):
    price = models.FloatField(default=10)
    follow_or_unfollow = models.BooleanField(default=True)
    contact = models.BooleanField(default=True)
    appointment = models.BooleanField(default=True)
    blogs = models.BooleanField(default=True)
    portfolio = models.BooleanField(default=True)
    skill = models.BooleanField(default=True)
    service = models.BooleanField(default=True)
    experience = models.BooleanField(default=True)
    testimonials = models.BooleanField(default=True)
