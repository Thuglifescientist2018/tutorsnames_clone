
from rest_framework import serializers
from account.models import ManageAddSkills, ManageAddSubSkills

# Create your models here.

# from app: account


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageAddSkills
        fields = '__all__'


class SubSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageAddSubSkills
        fields = "__all__"
