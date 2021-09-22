from django.db import models
from django.contrib.auth.models import (AbstractUser)
from django.forms import widgets
from colorfield.fields import ColorField


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
    # prefereneces
    profile_boolean = models.BooleanField(blank=True, null=True, default=False)
    follow_unfollow_boolean = models.BooleanField(
        blank=True, null=True, default=False)
    contact_boolean = models.BooleanField(blank=True, null=True, default=False)
    appointment_boolean = models.BooleanField(
        blank=True, null=True, default=False)
    skill_boolean = models.BooleanField(blank=True, null=True, default=False)
    service_boolean = models.BooleanField(blank=True, null=True, default=False)
    testimonial_boolean = models.BooleanField(
        blank=True, null=True, default=False)


class Fonts(models.Model):
    FONT_CHOICE = (
        ('select_font', 'Select Font'),
        ('tajawal', 'Tajawai'),
    )
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black")
    ]
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, default=1, null=True)
    site_font = models.CharField(
        max_length=255, blank=True, null=True, choices=FONT_CHOICE, default=1)
    site_color = ColorField(default='#FF0000')


class ManageServices(models.Model):
    service_name = models.CharField(max_length=255, blank=False, null=True)
    service_image = models.ImageField(upload_to='images/account/services/')
    service_details = models.TextField(blank=True, null=True)


class ManageSkills(models.Model):
    SKILLS_CHOICES = [
        ("Select_skills", "Select Skill"),
    ]
    SUB_SKILL_LEVELS = [
        ("ten_percent", "10%"),
        ("twenty_percent", "20%"),
        ("thirty_percent", "30%"),
        ("fourty_percent", "40%"),
        ("fifty_percent", "50%"),
        ("sixty_percent", "60%"),
        ("seventy_percent", "70%"),
        ("eighty_percent", "80%"),
        ("ninety_percent", "90%"),
        ("hundred_percent", "100%"),
    ]
    skill_name = models.CharField(blank=False, null=True, max_length=255)
    order = models.IntegerField(blank=True, null=True)
    skill_status = models.BooleanField(blank=True, null=False, default=True)
    service_details = models.TextField(blank=True, null=True)
    skills = models.CharField(blank=False, null=True,
                              choices=SKILLS_CHOICES, max_length=255)
    sub_skill_name = models.CharField(blank=False, null=True, max_length=255)
    sub_skill_level = models.CharField(
        blank=False, null=True, choices=SUB_SKILL_LEVELS, max_length=255)
    sub_order = models.IntegerField(blank=True, null=True)
    sub_skill_status = models.BooleanField(
        blank=True, null=False, default=True)


class ManageExperience(models.Model):
    EXPERIENCE_CHOICES = [
        ("Select_skills", "Select Experience"),
    ]
    experience_name = models.CharField(blank=False, null=True, max_length=255)
    order = models.IntegerField(blank=True, null=True)
    sub_experience = models.CharField(
        blank=False, null=True, choices=EXPERIENCE_CHOICES, max_length=255)
    sub_experience_name = models.CharField(
        blank=False, null=True, max_length=255)
    company_or_institute_name = models.CharField(
        blank=False, null=True, max_length=255)
    enter_date = models.DateField(blank=False, null=True)
    details = models.TextField(blank=False, null=True)
    sub_order = models.IntegerField(blank=False, null=True)


class ManageTestimonial(models.Model):
    client_name = models.CharField(blank=False, null=True, max_length=255)
    upload_client_avatar = models.ImageField(
        upload_to="images/account/testimonial/")
    feedback = models.TextField(blank=False, null=True)


class ManagePortfolio(models.Model):
    PORTFOLIO_CATEGORIES = [
        ("select", "Select"),
    ]
    category_name = models.CharField(blank=False, null=True, max_length=255)
    category = models.CharField(
        blank=False, null=True, choices=PORTFOLIO_CATEGORIES, max_length=255)
    title = models.CharField(blank=False, null=True, max_length=255)
    details = models.TextField(blank=False, null=True)
    project_link = models.URLField(blank=False, null=True)
    upload_image = models.ImageField(upload_to="images/account/portfolio/")


class ManageBlog(models.Model):
    BLOG_CATEGORIES = [
        ("select", "Select"),
    ]
    category_name = models.CharField(blank=False, null=True, max_length=255)
    category = models.CharField(
        blank=False, null=True, choices=BLOG_CATEGORIES, max_length=255)
    title = models.CharField(blank=False, null=True, max_length=255)
    slug = models.SlugField(blank=False, null=True)
    tags = models.CharField(blank=True, null=True, max_length=255)
    post_description = models.TextField(blank=True, null=True)
    upload_image = models.ImageField(upload_to="images/account/blog/")


class ManageAppointments(models.Model):
    appointment_booking_info_text = models.TextField(null=True, blank=True)
    saturday = models.BooleanField(blank=True, null=True)
    saturday_start_time = models.CharField(
        blank=True, null=True, max_length=255)
    saturday_end_time = models.CharField(blank=True, null=True, max_length=255)
    sunday = models.BooleanField(blank=True, null=True)
    sunday_start_time = models.CharField(blank=True, null=True, max_length=255)
    sunday_end_time = models.CharField(blank=True, null=True, max_length=255)
    monday = models.BooleanField(blank=True, null=True)
    monday_start_time = models.CharField(blank=True, null=True, max_length=255)
    monday_end_time = models.CharField(blank=True, null=True, max_length=255)
    tuesday = models.BooleanField(blank=True, null=True)
    tuesday_start_time = models.CharField(
        blank=True, null=True, max_length=255)
    tuesday_end_time = models.CharField(blank=True, null=True, max_length=255)
    wednesday = models.BooleanField(blank=True, null=True)
    wednesday_start_time = models.CharField(
        blank=True, null=True, max_length=255)
    wednesday_end_time = models.CharField(
        blank=True, null=True, max_length=255)
    thursday = models.BooleanField(blank=True, null=True)
    thursday_start_time = models.CharField(
        blank=True, null=True, max_length=255)
    thursday_end_time = models.CharField(blank=True, null=True, max_length=255)
    friday = models.BooleanField(blank=True, null=True)
    friday_start_time = models.CharField(blank=True, null=True, max_length=255)
    friday_end_time = models.CharField(blank=True, null=True, max_length=255)


class ManageUploadCV(models.Model):
    upload_pdf_file = models.FileField(upload_to="account/pdfs/cvs/")


class ManageChangePassword(models.Model):
    old_password = models.CharField(blank=False, null=True, max_length=255)
    new_password = models.CharField(blank=False, null=True, max_length=255)
    confirm_new_password = models.CharField(
        blank=False, null=True, max_length=255)
