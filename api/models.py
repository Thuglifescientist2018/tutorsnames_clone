from rest_framework import serializers
from account.models import ManageSkills

# Create your models here.

# from app: account


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageSkills
        fields = '__all__'
