from django.urls import path
from .views import AccountSkills, AccountSkillsAll, AccountSubSkillAll, AccountSubSkills

urlpatterns = [
    path('skills/', AccountSkills.as_view(), name="api_skills"),
    path('subskills/', AccountSubSkills.as_view(), name="api_sub_skills"),
    path('skills_all/', AccountSkillsAll.as_view(), name="api_skills_all"),
    path('subskills_all/', AccountSubSkillAll.as_view(), name="api_skills_all"),

]
