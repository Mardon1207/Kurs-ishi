from rest_framework import serializers
from .models import Listing, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ListingSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Kategoriyani ID orqali olish
    latitude = serializers.FloatField(required=False)  # Joylashuv koordinatalari
    longitude = serializers.FloatField(required=False)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'location', 'latitude', 'longitude', 'category', 'owner', 'image']
        extra_kwargs = {'owner': {'read_only': True}}

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
