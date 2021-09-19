from account.models import ManageSkills
from django.db.models import fields
from django.http.response import JsonResponse
from .models import SkillsSerializer


# Create your views here.


def accountskills(request):
    skills = ManageSkills.objects.all()
    serializer = SkillsSerializer(skills, many=True)
    return JsonResponse(serializer.data, safe=False)
