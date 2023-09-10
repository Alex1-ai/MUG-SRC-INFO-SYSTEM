from rest_framework import serializers
from .models import Src_News



class Src_News_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Src_News
        fields = ["id","title", "description", "image", "updated_at"]





