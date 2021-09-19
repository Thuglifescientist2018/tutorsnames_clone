from django.contrib import admin
from .models import (User, Fonts, ManageServices, ManageSkills, ManageExperience, ManageTestimonial,
                     ManagePortfolio, ManageBlog, ManageAppointments, ManageUploadCV, ManageChangePassword)
# Register your models here.

admin.site.register(User)
admin.site.register(Fonts)
admin.site.register(ManageServices)
admin.site.register(ManageSkills)
admin.site.register(ManageExperience)
admin.site.register(ManageTestimonial)
admin.site.register(ManagePortfolio)
admin.site.register(ManageBlog)
admin.site.register(ManageAppointments)
admin.site.register(ManageUploadCV)
admin.site.register(ManageChangePassword)
