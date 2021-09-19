
from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from account.models import User
from .models import (Fonts,
                     ManageServices, ManageSkills, ManageExperience, ManageTestimonial, ManagePortfolio,
                     ManageBlog, ManageAppointments, ManageUploadCV, ManageChangePassword
                     )


class ManageProfileForm(ModelForm):

    class Meta:
        model = User
        fields = ["full_name", "designation",
                  "email", "phone", "about_me", "profile_boolean", "follow_unfollow_boolean", "contact_boolean", "appointment_boolean", "skill_boolean", "service_boolean", "testimonial_boolean"]


class ManageFontsForm(ModelForm):
    class Meta:
        model = Fonts
        fields = "__all__"


class ManageServicesForm(ModelForm):
    class Meta:
        model = ManageServices
        fields = "__all__"


class ManageSkillsForm(ModelForm):
    class Meta:
        model = ManageSkills
        fields = "__all__"


class ManageExperienceForm(ModelForm):
    class Meta:
        model = ManageExperience
        fields = "__all__"


class ManageTestimonialForm(ModelForm):
    class Meta:
        model = ManageTestimonial
        fields = "__all__"


class ManagePortfolioForm(ModelForm):
    class Meta:
        model = ManagePortfolio
        fields = "__all__"


class ManageBlogForm(ModelForm):
    class Meta:
        model = ManageBlog
        fields = "__all__"


class ManageAppointmentsForm(ModelForm):
    class Meta:
        model = ManageAppointments
        fields = "__all__"


class ManageUploadCVForm(ModelForm):
    class Meta:
        model = ManageUploadCV
        fields = "__all__"


class ManageChangePasswordForm(ModelForm):
    class Meta:
        model = ManageChangePassword
        fields = "__all__"
