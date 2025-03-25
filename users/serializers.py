from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)  # 🔹 Profil rasmi ixtiyoriy

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'region', 'district', 'profile_image']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)  # 🔹 create_user dan foydalanamiz
        return user
