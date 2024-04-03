from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', LoginView.as_view(), name='login_page'),
    path('logout', logout_view, name='logout_page'),
    path('signup', SignupView.as_view(), name='signup_page'),
]
