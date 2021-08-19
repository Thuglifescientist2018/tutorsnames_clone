from django.db.models.base import Model
from django.forms import ModelForm
from .models import UpdateInfo
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(ModelForm):
    class Meta:
        model = UserCreationForm
        fields = ["name", "email", "password", "country"]
