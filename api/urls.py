from api.views import accountskills
from django.urls import path

urlpatterns = [
    path('accountskills/', accountskills, name="accountskills")

]
