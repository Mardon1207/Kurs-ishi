from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer


# ✅ Ro‘yxatdan o‘tish (Registratsiya)
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # ❗️Hamma ro‘yxatdan o‘ta olishi kerak


# ✅ Login qilish (JWT Token yaratish)
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get("username")  # 📌 Login uchun username yoki email
        password = attrs.get("password")

        # 🔍 Avval username orqali qidiramiz
        user = CustomUser.objects.filter(username=username_or_email).first()
        
        # 🔍 Agar username topilmasa, email orqali qidiramiz
        if user is None:
            user = CustomUser.objects.filter(email=username_or_email).first()
        
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


# ✅ Foydalanuvchi profili (User Profile API)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user

    data = {
        "first_name": user.first_name if user.first_name else None,
        "last_name": user.last_name if user.last_name else None,
        "email": user.email,
        "username": user.username,
        "phone_number": user.phone_number if user.phone_number else None,
        "region": user.region if user.region else None,
        "district": user.district if user.district else None,
        "profile_image": request.build_absolute_uri(user.profile_image.url) if user.profile_image else None
    }

    return Response(data)
