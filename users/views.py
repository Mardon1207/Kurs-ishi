from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
