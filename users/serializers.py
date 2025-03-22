from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'user_type', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # ✅ Parolni hash qilish
        return super().create(validated_data)
