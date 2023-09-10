from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.db import transaction
# from rest_framework.permissions import IsAdminUser

from .models import Position, Candidate, Vote
from .serializers import CandidateSerializer,PositionSerializer,VoteSerializer


@api_view(['GET'])
def positionsViewSet(request):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer(queryset, many=True)

    return Response(serializer_class.data)

# @api_view()
# def candidateViewSet(request):
#      queryset = Candidate.objects.select_related('position').all().order_by('-vote')
#      serializer_class = CandidateSerializer(queryset,many=True)
#     #  permission_classes = [IsAdminUser, ]
#      return Response(serializer_class.data)
@api_view(['GET'])
def candidate_list(request):
    try:
        # Fetch the candidates ordered by 'vote' field and include the related 'position'
        queryset = Candidate.objects.select_related('position').order_by('-votes')
        serializer = CandidateSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view()
def candidate_details(request, pk):
    candidate = get_object_or_404(
        Candidate.objects.filter(pk=pk)
    )
    serializer  = CandidateSerializer(candidate)
    return Response(serializer.data)


# Create your views here.
@api_view(['POST', 'GET'])
# @permission_classes([IsAuthenticated])
def castVoteView(request):
    if request.method == 'POST':
        try:
            data = request.data
            email = data.get("email", "")
            candidate_ids = data.get("candidate_ids", [])
            
            # Check if the user has already voted for any candidate
            if Vote.objects.filter(email=email).exists():
                raise Exception( "You have already voted.")

            with transaction.atomic():
                for candidate_id in candidate_ids:
                    try:
                        candidate = Candidate.objects.get(pk=candidate_id)
                        position = candidate.position
                        print(candidate, position)

                        # Check if the user has already voted for a candidate in this position
                        if Vote.objects.filter(email=email, candidate__position=position).exists():
                            raise Exception( f"You have already voted for a candidate in the {position} position.",
                                            )
                        #    raise Exception({"error": f"You have already voted for a candidate in the {position} position."},
                        #                     status=status.HTTP_400_BAD_REQUEST)

                        # Create a new vote and update the vote count for the candidate
                        Vote.objects.create(email=email, candidate=candidate)
                        candidate.votes += 1
                        candidate.save()
                    except (Candidate.DoesNotExist, Position.DoesNotExist):
                        raise Exception( "Invalid candidate or position.")
                        # raise Exception({"error": "Invalid candidate or position."}, status=status.HTTP_404_NOT_FOUND)

            return Response({"message": "Votes cast successfully!"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": f"Failed to cast votes: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response("OK")
# @api_view(['GET','POST'])
# # @permission_classes([IsAuthenticated])
# def castVoteView(request):
#     if request.method == 'POST':
#         print(request.data)
#         votes = request.data["candidate"]
#         print(votes)

#         serializer = VoteSerializer(data=request.data)
#         # if serializer.is_valid():
#         print("Here")
#         serializer.is_valid(raise_exception=True )
#         print("after")
#         print(serializer.validated_data)
#         #
#         # # return Response(serializer.data, status.HTTP_201_CREATED)
#         email =serializer.validated_data["email"]
#         candidateVote = serializer.validated_data["candidate"]
         
#         print(email)
#         print(candidateVote)
#         # return Response("Ok")
#         # return Response(serializer.data, status.HTTP_201_CREATED)
#         # return Response("ok")
#             # user = request.user
#             # votes = request.data.get('votes', [])  # Expected format: [{"position_id": 1, "candidate_id": 1}, ...]

#         # for vote_data in votes:
#         #     position_id = vote_data.get('position_id')
#         #     candidate_id = vote_data.get('candidate_id')

#         try:
#             position = Position.objects.get(pk=candidateVote.position_id)
#             candidate = Candidate.objects.get(pk=candidateVote.id, position=position)
#         except (Position.DoesNotExist, Candidate.DoesNotExist):
#             return Response({"error": "Invalid position or candidate."}, status=status.HTTP_404_NOT_FOUND)

#                 # Check if the user has already voted for a candidate in this position
#         if Vote.objects.filter(email=email, candidate__position=position).exists():
#             return Response({"error": f"You have already voted for a candidate in the {position} position."},
#                                     status=status.HTTP_400_BAD_REQUEST)

#                 # If the user hasn't voted for a candidate in this position, save the vote and update the vote count
#         Vote.objects.create(email=email, candidate=candidate)
#         candidate.votes += 1
#         candidate.save()

#         return Response({"message": "Votes cast successfully!"}, status=status.HTTP_201_CREATED)
#         # else:
#         #     # If the object that is to be serialized is bad
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response("OK")
             
        