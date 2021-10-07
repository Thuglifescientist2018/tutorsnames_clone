from re import template
from django.db.models import query
from django.db.models.fields import files
from django.http import request
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.urls.base import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView, TemplateView, ListView
from django.views.generic.edit import DeleteView
from .models import (ManageAddSkills, ManageAddSubSkills, User, Fonts, ManageServices,  ManageExperience,
                     ManageTestimonial, ManagePortfolio, ManageBlog, ManageAppointments, ManageUploadCV)
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from .forms import (ManageAddSubSkillsForm, ManageProfileForm, ManageFontsForm, ManageServicesForm, ManageAddSkillsForm, ManageExperienceForm,
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
    # with out get_object() it filled the form with+  queryset = User.objects.all()
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


def Skills(request):
    template_name = 'account/sidebar/skills.html'
    form = ManageAddSkillsForm(request.POST or None)
    form2 = ManageAddSubSkillsForm(request.POST or None)
    if form2.is_valid():
        form2.save()

    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "form2": form2,
        "skills": ManageAddSkills.objects.all(),
        "sub_skills": ManageAddSubSkills.objects.all()

    }
    return render(request, template_name, context)


class SkillDelete(DeleteView):
    model = ManageAddSkills
    template_name = 'account/sidebar/deletes/skill_delete.html'
    success_url = reverse_lazy('skills')


def SkillActivate(request, pk):
    obj = get_object_or_404(ManageAddSkills, pk=pk)
    obj.skill_status = True
    obj.save()

    return redirect(reverse_lazy('skills'))


def SkillDeactivate(request, pk):
    obj = get_object_or_404(ManageAddSkills, pk=pk)
    obj.skill_status = False
    obj.save()
    return redirect(reverse_lazy('skills'))


class SkillEdit(UpdateView):
    model = ManageAddSkills
    fields = "__all__"
    success_url = reverse_lazy('skills')
    template_name = "account/sidebar/edits/skilledit.html"


class SubSkillEdit(UpdateView):
    model = ManageAddSubSkills
    fields = ['skills', 'sub_skill_name', 'sub_skill_level', 'sub_order']
    success_url = reverse_lazy('skills')
    template_name = "account/sidebar/edits/sub_skill_edit.html"


class SubSkillDelete(DeleteView):
    model = ManageAddSubSkills
    template_name = "account/sidebar/deletes/subskill_delete.html"
    success_url = reverse_lazy("skills")


def SubSKillActivate(request, pk):
    sub_skill = ManageAddSubSkills.objects.get(id=pk)
    sub_skill.sub_skill_status = True
    sub_skill.save()
    return redirect(reverse_lazy('skills'))


def SubSkillDeactivate(request, pk):
    sub_skill = ManageAddSubSkills.objects.get(id=pk)
    sub_skill.sub_skill_status = False
    sub_skill.save()
    return redirect(reverse_lazy('skills'))


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


def log_in(request):
    template_name = 'account/login.html'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')

    return render(request, template_name)


def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect('/')
