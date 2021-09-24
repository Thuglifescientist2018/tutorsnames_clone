from account.models import ManageAddSkills, ManageAddSubSkills
from django.db.models import fields
from django.http.response import JsonResponse
from .models import SkillsSerializer, SubSkillsSerializer


# Create your views here.


def accountskills(request):
    skills = ManageAddSkills.objects.all()
    serializer = SkillsSerializer(skills, many=True)
    return JsonResponse(serializer.data, safe=False)


def accountsubskills(request):
    sub_skills = ManageAddSubSkills.objects.all()
    serializer = SubSkillsSerializer(sub_skills, many=True)
    return JsonResponse(serializer.data, safe=False)
