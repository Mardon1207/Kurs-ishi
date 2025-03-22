from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Foydalanuvchi faqat o‘zining xabarlarini ko‘radi"""
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)

    def perform_create(self, serializer):
        """Xabar yuborishda avtomatik ravishda sender qo‘shiladi"""
        serializer.save(sender=self.request.user)
