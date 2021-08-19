from users.models import UpdateInfo, SocialSettings
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView


# Create your views here.


class Users(ListView):
    model = UpdateInfo
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['socials'] = SocialSettings.objects.all()
        return context
