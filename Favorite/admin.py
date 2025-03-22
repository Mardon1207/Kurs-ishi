from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing', 'created_at')  # ✅ Sevimlilarni ro‘yxatda ko‘rsatish
    search_fields = ('user__username', 'listing__title')  # ✅ Qidiruv qo‘shish
