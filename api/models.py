from django.db import models
from rest_framework import serializers
from account.models import ManageAddSkills, ManageAddSubSkills


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageAddSkills
        fields = "__all__"


class SubSkillsSerializer(serializers.ModelSerializer):
    # foreign key = skills so skills refers to the model manageaddskills and then accessing its field skill_name
    skills = serializers.CharField(source='skills.skill_name', allow_null=True)

    class Meta:
        model = ManageAddSubSkills
        fields = "__all__"


class ChangePageSize(models.Model):
    page_size = models.CharField(
        blank=True, null=True, max_length=255, default=5)
