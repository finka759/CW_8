from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'id',
            'email',
            'phone',
            'password',
            'token',
            'chat_id',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        ]
