from rest_framework import serializers

from .models import Position,Candidate,Vote


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ["id", "name", "description"]
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=250)

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "image", "votes", "department", "position"]
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=100)
    # image = serializers.ImageField()
    # votes = serializers.IntegerField()
    # department = serializers.CharField(max_length=150)
    position = serializers.StringRelatedField()
    # position = PositionSerializer()

    #  ADDING A VALIDATORs on your serializer
    # def validate(self, data):
    #     if data["password"] != data["comfirm_password"]:
    #         return serializers.ValidationError("Password and comfirm password does not match")
    #     return data
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["email", "candidate"]
    # def validate(self, data):
    #     user = data['user']
    #     candidate = data['candidate']

    #     # Check if the user has already voted for the candidate
    #     if Vote.objects.filter(user=user, candidate=candidate).exists():
    #         raise serializers.ValidationError(
    #             f"You have already votedededed for a candidate in the {candidate.position} position."
    #         )

    #     return data