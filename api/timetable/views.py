from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Timetable, MugDepartment
from rest_framework.response import Response

from .serializers import MugDepartmentSerializer,TimetableSerializer
# Create your views here.
@api_view()
def timetableViewSet(request):
     queryset = Timetable.objects.all().select_related("department").order_by('-updated_at')
     serializer_class = TimetableSerializer(queryset,many=True)
    #  permission_classes = [IsAdminUser, ]
     return Response(serializer_class.data)