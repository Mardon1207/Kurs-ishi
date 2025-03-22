from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user', 'rating', 'created_at')
    readonly_fields = ('user',)  # ✅ User maydoni endi faqat o‘qish uchun bo‘ladi

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Faqat yangi sharh qo‘shilayotganda
            obj.user = request.user  # ✅ Foydalanuvchini avtomatik qo‘shish
        super().save_model(request, obj, form, change)

admin.site.register(Review, ReviewAdmin)
