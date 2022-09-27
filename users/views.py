from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

from users.serializers import CustomUserDetailsSerializer


class CustomRegisterView(RegisterView):
    pass


class CustomLoginView(LoginView):
    pass


class CustomUserDetailsView(UserDetailsView):
    pass


CustomRegisterView = CustomRegisterView.as_view()
CustomLoginView = CustomLoginView.as_view()
CustomUserDetailsView = CustomUserDetailsView.as_view()


def jwt_response_payload_handler(token, user=None, request=None, *args, **kwargs):
    return {
        'token': token,
        'user': CustomUserDetailsSerializer(user, context={'request': request}).data,
    }
