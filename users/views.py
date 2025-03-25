from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# ✅ Login uchun JWT Token yaratish
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")  # 📌 Login faqat username orqali
        password = attrs.get("password")

        user = CustomUser.objects.filter(username=username).first()

        if user is None:
            raise serializers.ValidationError("Foydalanuvchi topilmadi!")

        if not user.check_password(password):
            raise serializers.ValidationError("Parol noto‘g‘ri!")

        attrs["username"] = user.username
        data = super().validate(attrs)
        data["user_type"] = user.user_type if hasattr(user, "user_type") else "default"
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "username": user.username,
        "phone": user.profile.phone if hasattr(user, 'profile') else None,
        "region": user.profile.region if hasattr(user, 'profile') else None,
        "district": user.profile.district if hasattr(user, 'profile') else None,
        "profile_image": request.build_absolute_uri(user.profile.profile_image.url) if hasattr(user, 'profile') and user.profile.profile_image else None
    }
    return Response(data)