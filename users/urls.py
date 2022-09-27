from django.urls import path
from dj_rest_auth.registration.views import VerifyEmailView

from users.views import CustomRegisterView, CustomLoginView, CustomUserDetailsView
from rest_framework_simplejwt.views import token_refresh, token_verify

urlpatterns = [
    # path('auth/', include('dj_rest_auth.urls'))
    path('auth/signup/', CustomRegisterView, name='rest_register'),
    path('auth/login/', CustomLoginView, name='rest_login'),
    path('auth/user/', CustomUserDetailsView, name='rest_user'),
    path('auth/verify_token/', token_verify, name='verify_jwt_token'),
    path('auth/refresh_token/', token_refresh, name='refresh_jwt_token'),
    path(
        'auth/email/confirm/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent',

    ),

]