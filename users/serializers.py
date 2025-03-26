from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'first_name', 'last_name', 'email', 'username', 'password',
            'user_type', 'phone_number', 'region', 'district', 'profile_image'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            user_type=validated_data.get('user_type', 'renter'),
            phone_number=validated_data.get('phone_number', None),
            region=validated_data.get('region', None),
            district=validated_data.get('district', None),
            profile_image=validated_data.get('profile_image', None)
        )
        return user
