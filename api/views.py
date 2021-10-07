from django.db.models.query import QuerySet
from account.models import ManageAddSkills, ManageAddSubSkills
from django.http.response import JsonResponse
from .models import SkillsSerializer, SubSkillsSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class ASkillsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'


class ASubSkillsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'


class AccountSkills(ListAPIView):
    queryset = ManageAddSkills.objects.all()
    serializer_class = SkillsSerializer
    pagination_class = ASkillsPagination


class AccountSubSkills(ListAPIView):
    queryset = ManageAddSubSkills.objects.all()
    serializer_class = SubSkillsSerializer
    pagination_class = ASubSkillsPagination


class AccountSkillsAll(ListAPIView):
    queryset = ManageAddSkills.objects.all()
    serializer_class = SkillsSerializer


class AccountSubSkillAll(ListAPIView):
    queryset = ManageAddSubSkills.objects.all()
    serializer_class = SubSkillsSerializer
