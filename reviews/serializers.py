from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'listing', 'rating', 'comment', 'created_at', 'user']
        extra_kwargs = {'user': {'read_only': True}}  # ✅ User avtomatik bo‘ladi
        
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Reyting 1 dan 5 gacha bo‘lishi kerak.")
        return value