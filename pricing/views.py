from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import MonthlyStudent, MonthlyTutor, MonthlyPro, YearlyStudent, YearlyTutor, YearlyPro
# Create your views here.


class Pricing(TemplateView):
    template_name = 'pricing.html'
    monthlyStudent = MonthlyStudent()
    monthlyTutor = MonthlyTutor()
    monthlyPro = MonthlyPro()

    yearlyStudent = YearlyStudent()
    yearlyTutor = YearlyTutor()
    yearlyPro = YearlyPro()
    extra_context = {"monthlyStudent": monthlyStudent, "monthlyTutor": monthlyTutor, "monthlyPro": monthlyPro,
                     "yearlyStudent": yearlyStudent, "yearlyTutor": yearlyTutor, "yearlyPro": yearlyPro}
