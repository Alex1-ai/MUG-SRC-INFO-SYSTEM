from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Src_News
from rest_framework.response import Response
from .serializers import Src_News_Serializer
# Create your views here.
@api_view()
def srcNewsViewSet(request):
     queryset = Src_News.objects.all().order_by('-updated_at')
     serializer_class = Src_News_Serializer(queryset,many=True)
    #  permission_classes = [IsAdminUser, ]
     return Response(serializer_class.data)