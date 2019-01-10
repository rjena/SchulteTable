from rest_framework import serializers
from .models import UserST, Test

class UserSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserST
        fields = ('id', 'login', 'email', 'name', 'bday', 'password',
                  'tokenToConfirmEmail', 'tokenToResetPassword')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'date', 'user_id', 'age', 'stWE', 'stWU', 'stPS')
