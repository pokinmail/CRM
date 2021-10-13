from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, get_my_team, add_member, TraceTeam

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

# generate leads/id/

urlpatterns = [
    
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/add_member/', add_member, name='add_member'),
    path('teams/trace/', TraceTeam.as_view(), name='trace'),
    path('', include(router.urls)),
]

'''
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('teams/add_profile/', add_profile, name='add_profile'),
    #gets all user profiles and create a new profile
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    #retrieves profile details of the currently logged in user
    path("profile/<int:pk>",UserProfileDetailView.as_view(),name="profile"),
'''