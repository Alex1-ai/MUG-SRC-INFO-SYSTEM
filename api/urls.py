from django.urls import path, include
from rest_framework.authtoken import views
from .views import home


urlpatterns = [
    path('', home, name='api.home'),
    path('poll/', include('api.poll.urls')),
    path('news/', include('api.src_news.urls')),
    path('poster/', include('api.campus_billboard.urls')),
    path('timetable/', include('api.timetable.urls')),
    path('auth/', include('api.account.urls')),
    

]