from django.contrib import admin
from .models import (MonthlyStudent, MonthlyTutor, MonthlyPro,
                     YearlyStudent, YearlyTutor, YearlyPro)
# Register your models here.

admin.site.register(MonthlyStudent)
admin.site.register(MonthlyTutor)
admin.site.register(MonthlyPro)

admin.site.register(YearlyStudent)
admin.site.register(YearlyTutor)
admin.site.register(YearlyPro)
