from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'region', 'district', 'profile_image']
        extra_kwargs = {
            'password': {'write_only': True},  # ✅ Parolni faqat yozish mumkin
            'email': {'required': True},  # ✅ Email majburiy maydon
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)  # ✅ Parolni xavfsiz saqlash
        user.save()
        return user
