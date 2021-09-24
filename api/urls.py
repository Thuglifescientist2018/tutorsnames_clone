from api.views import accountskills, accountsubskills
from django.urls import path

urlpatterns = [
    path('accountskills/', accountskills, name="accountskills"),
    path('accountsubskills/', accountsubskills, name="accountsubskills")

]
