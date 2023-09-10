from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import BillBoard
from rest_framework.response import Response
from .serializers import BillBoard_Serializer
# Create your views here.
@api_view()
def billBoardViewSet(request):
     queryset = BillBoard.objects.all().order_by('-updated_at')
     serializer_class = BillBoard_Serializer(queryset,many=True)
    #  permission_classes = [IsAdminUser, ]
     return Response(serializer_class.data)