from django.db.models import query
from django.http import request
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.views.generic import UpdateView, TemplateView, ListView
from .models import (ManageSkills, User, Fonts, ManageServices, ManageSkills, ManageExperience,
                     ManageTestimonial, ManagePortfolio, ManageBlog, ManageAppointments, ManageUploadCV)
from django import forms
from django.shortcuts import get_object_or_404, redirect
from .forms import (ManageProfileForm, ManageFontsForm, ManageServicesForm, ManageSkillsForm, ManageExperienceForm,
                    ManageTestimonialForm, ManagePortfolioForm, ManageBlogForm, ManageAppointmentsForm, ManageUploadCVForm, ManageChangePasswordForm
                    )
from pricing.models import MonthlyStudent, MonthlyTutor, MonthlyPro, YearlyStudent, YearlyTutor, YearlyPro
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
    # with out get_object() it filled the form with  queryset = User.objects.all()
    success_url = reverse_lazy("manage-profile", args=[2])

    def get_object(self):
        id_ = self.request.user.id
        print(id_)
        return get_object_or_404(User, id=id_)


class ManageSubscription(TemplateView):
    template_name = "account/sidebar/subscription.html"
    monthlyStudent = MonthlyStudent()
    monthlyTutor = MonthlyTutor()
    monthlyPro = MonthlyPro()

    yearlyStudent = YearlyStudent()
    yearlyTutor = YearlyTutor()
    yearlyPro = YearlyPro()
    extra_context = {"monthlyStudent": monthlyStudent, "monthlyTutor": monthlyTutor, "monthlyPro": monthlyPro,
                     "yearlyStudent": yearlyStudent, "yearlyTutor": yearlyTutor, "yearlyPro": yearlyPro}


class Layouts(TemplateView):
    template_name = "account/sidebar/layouts.html"


class FontsManage(UpdateView):
    form_class = ManageFontsForm
    template_name = "account/sidebar/fonts.html"

    def get_object(self):

        id_ = Fonts.objects.all().last().id
        if id_:
            return get_object_or_404(Fonts, id=id_)
        elif not id_:
            Fonts.objects.create(user=User, site_font=1, site_color="#fff")


# users upload multiple services.

class Services(CreateView):
    form_class = ManageServicesForm
    template_name = 'account/sidebar/services.html'

    def get_object(self):
        id_ = ManageServices.objects.all().last().id
        if id_:
            return get_object_or_404(ManageServices, id=id_)
        elif not id_:
            queryset = ManageSkills


class Skills(CreateView):
    form_class = ManageSkillsForm
    template_name = 'account/sidebar/skills.html'
    success_url = reverse_lazy("skills")


class Experience(UpdateView):
    form_class = ManageExperienceForm

    def get_object(self):
        id_ = ManageSkills  .objects.all().last().id
        if id_:
            return get_object_or_404(ManageSkills, id=id_)
    template_name = 'account/sidebar/experience.html'


class Testimonial(UpdateView):
    form_class = ManageTestimonialForm
    template_name = 'account/sidebar/testimonial.html'


class Portfolio(UpdateView):
    form_class = ManageProfileForm
    template_name = 'account/sidebar/portfolio.html'


class Blog(UpdateView):
    form_class = ManageBlogForm
    template_name = 'account/sidebar/blog.html'


class Appointments(UpdateView):
    form_class = ManageAppointmentsForm
    template_name = 'account/sidebar/appointments.html'


class ContactMessages(ListView):
    template_name = 'account/sidebar/contact_messages.html'


class UploadCV(UpdateView):
    form_class = ManageUploadCVForm
    template_name = 'account/sidebar/upload_cv.html'


class ChangePassword(UpdateView):
    form_class = ManageChangePasswordForm
    template_name = 'account/sidebar/change_password.html'
