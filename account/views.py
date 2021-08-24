from django.http import request
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import User
from django import forms
from django.shortcuts import get_object_or_404
from .forms import ManageProfileForm
# Create your views here.


class CreateProfile(CreateView):
    model = User
    fields = ['full_name', 'email', 'username', 'password', 'select_country']

    template_name = "account/registration.html"
    success_url = reverse_lazy("homepage")

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CreateProfile, self).get_form(form_class)
        form.fields['full_name'].widget = forms.TextInput(
            attrs={'placeholder': 'Your name'})
        form.fields['username'].widget = forms.TextInput(
            attrs={'placeholder': 'User Name'})
        form.fields['email'].widget = forms.TextInput(
            attrs={'placeholder': 'Email'})
        form.fields['password'].widget = forms.TextInput(
            attrs={'type': 'password', 'placeholder': 'Password'})

        return form


class ManageProfile(UpdateView):

    template_name = 'account/manage_profile.html'
    form_class = ManageProfileForm
    success_url = '/'

    def get_object(self):
        id_ = self.request.user.id
        print(id_)
        return get_object_or_404(User, id=id_)
