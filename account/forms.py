from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from account.models import User
from .models import Fonts


class ManageProfileForm(ModelForm):

    class Meta:
        model = User
        fields = ["full_name", "designation",
                  "email", "phone", "about_me", "profile_boolean", "follow_unfollow_boolean", "contact_boolean", "appointment_boolean", "skill_boolean", "service_boolean", "testimonial_boolean"]


class ManageFontsForm(ModelForm):
    class Meta:
        model = Fonts
        fields = "__all__"
