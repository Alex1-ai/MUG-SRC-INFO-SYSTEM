from rest_framework import routers
from django.urls import path, include


from .import views

# router = routers.DefaultRouter()
# router.register(r"/candidates" ,views.CandidateViewSet)


urlpatterns = [
    path('', views.castVoteView),
    path('candidates/', views.candidate_list),
    path('candidate/<int:pk>', views.candidate_details),
    path('positions/', views.positionsViewSet)
]


