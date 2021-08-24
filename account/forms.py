from django.db.models import fields
from django.forms import ModelForm
from account.models import User


class ManageProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ["full_name", "designation",
                  "password", "email", "phone", "about_me"]
