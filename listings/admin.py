from django.contrib import admin
from .models import Category, Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'location', 'is_available', 'created_at')  # ✅ is_available qo‘shildi
    list_filter = ('is_available', 'location')  # ✅ Faqat Field nomlari ishlatilishi kerak

admin.site.register(Listing, ListingAdmin)

admin.site.register(Category)