from django.urls import path
from .views import FavoriteCreateView, FavoriteListView, FavoriteDeleteView

urlpatterns = [
    path('', FavoriteListView.as_view(), name='favorite-list'),  # ✅ Sevimlilarni olish
    path('add/', FavoriteCreateView.as_view(), name='favorite-add'),  # ✅ Sevimlilarga qo‘shish
    path('<int:pk>/delete/', FavoriteDeleteView.as_view(), name='favorite-delete'),  # ✅ Sevimlidan o‘chirish
]
