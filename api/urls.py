from django.urls import path
from .views import AccountSkills,  AccountSubSkills

urlpatterns = [
    path('skills/', AccountSkills.as_view(), name="api_skills"),
    path('subskills/', AccountSubSkills.as_view(), name="api_sub_skills"),
]
