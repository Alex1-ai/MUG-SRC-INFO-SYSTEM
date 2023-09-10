from rest_framework import serializers

from .models import Timetable,MugDepartment

class MugDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MugDepartment
        fields = ["id","departmentName", "updated_at"]


class TimetableSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    class Meta:
        model = Timetable
        fields = ["id","name", "timetableDoc","department","updated_at"]

        # department = MugDepartment.departmentName

        