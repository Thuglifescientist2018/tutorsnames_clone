from django.db.models.query import QuerySet
from rest_framework import serializers
from account.models import ManageAddSkills, ManageAddSubSkills
from django.http.response import JsonResponse
from .models import SkillsSerializer, SubSkillsSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class ASkillsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.request.query_params.get('page', None),
            'results': data
        })


class ASubSkillsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.request.query_params.get('page', None),
            'results': data
        })


class AccountSkills(ListAPIView):
    queryset = ManageAddSkills.objects.all().order_by('-pk')
    serializer_class = SkillsSerializer
    pagination_class = ASkillsPagination


class AccountSubSkills(ListAPIView):
    queryset = ManageAddSubSkills.objects.all().order_by('-pk')
    serializer_class = SubSkillsSerializer
    pagination_class = ASubSkillsPagination
