from django.contrib import admin
from .models import SocialSettings, UpdateInfo
# Register your models here.
admin.site.register(UpdateInfo)
admin.site.register(SocialSettings)
