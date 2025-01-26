from django.urls import path
from .views import login_user, register_user
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]