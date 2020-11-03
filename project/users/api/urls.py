from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import registration_api_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', registration_api_view, name="register_api"),
    path('login', obtain_auth_token, name="login_api"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
