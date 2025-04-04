from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView,user_profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ To‘g‘ri login URL
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', user_profile, name='user_profile'),
]
