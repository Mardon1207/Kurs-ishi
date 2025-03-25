from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# ✅ Login uchun JWT Token yaratish
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get("username")
        password = attrs.get("password")

        # 🔹 Username yoki email orqali foydalanuvchini topish
        user = CustomUser.objects.filter(email=username_or_email).first() or CustomUser.objects.filter(username=username_or_email).first()

        if user is None:
            raise serializers.ValidationError("Foydalanuvchi topilmadi!")

        # 🔹 Parolni tekshirish
        if not user.check_password(password):
            raise serializers.ValidationError("Parol noto‘g‘ri!")

        # 🔹 JWT Token yaratish
        attrs["username"] = user.username
        data = super().validate(attrs)
        data["user_type"] = user.user_type if hasattr(user, "user_type") else "default"
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
