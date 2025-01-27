from django.urls import path
from .views import login_user, register_user, validate_token, refresh_token, logout_user

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user'),
    path('token/validate/', validate_token, name='token_validate'),
    path('token/refresh/', refresh_token, name='refresh_token'),
]