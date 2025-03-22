from django.contrib import admin
from .models import Message  # Message modelini import qilish

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "content", "timestamp")
    search_fields = ("sender__username", "receiver__username", "content")

# Yoki shunchaki:
# admin.site.register(Message)
