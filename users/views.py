from rest_framework import generics
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
        data = super().validate(attrs)
        data['user_type'] = self.user.user_type  # Foydalanuvchi turini qaytaramiz
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
