from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('',index),
    path('register',register, name='register'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),

    path('user/profile', profile, name='profile'),
    path('user/interests', interests, name='interests'),
    path('user/skills', skills, name='skills'),

    path('interests/search', search_interests, name='search_interests'),
    path('skills/search', search_skills, name='search_skills'),
]