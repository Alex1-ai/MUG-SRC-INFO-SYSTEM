from rest_framework import serializers

from .models import BillBoard

class BillBoard_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BillBoard
        fields = ["id","poster_img", "updated_at"]