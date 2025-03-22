from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'listing', 'created_at']
        extra_kwargs = {'user': {'read_only': True}}  # ✅ Foydalanuvchi avtomatik qo‘shiladi
