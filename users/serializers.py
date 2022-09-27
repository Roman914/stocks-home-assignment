from dj_rest_auth.serializers import LoginSerializer
from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework import serializers as rfs

from users.models import User


class CustomUserDetailsSerializer(rfs.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
        )
        read_only_fields = ('id', 'email', 'farms')

    @staticmethod
    def get_can_toggle_wand(user):
        if farm := user.farms.last():
            if farm.location.country in ('US',):
                return True
        return False


class UserSerializer0(rfs.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  )
        read_only_fields = ('id', 'email', 'country')


# noinspection PyAbstractClass
class CustomLoginSerializer(LoginSerializer):
    username = None


# noinspection PyAbstractClass
class CustomJWTSerializer(rfs.Serializer):
    access_token = rfs.CharField()
    refresh_token = None
    user = CustomUserDetailsSerializer()

    def get_user(self, obj):
        """
        Required to allow using custom USER_DETAILS_SERIALIZER in
        JWTSerializer. Defining it here to avoid circular imports
        """
        rest_auth_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})

        JWTUserDetailsSerializer = import_string(
            rest_auth_serializers.get(
                'USER_DETAILS_SERIALIZER',
                'dj_rest_auth.serializers.UserDetailsSerializer',
            ),
        )

        user_data = JWTUserDetailsSerializer(obj['user'], context=self.context).data
        return user_data
