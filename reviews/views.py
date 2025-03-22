from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer
from listings.models import Listing  # ✅ E’lon modelini import qilish

# ✅ Sharh yaratish (faqat login qilgan foydalanuvchilar)
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Faqat login foydalanuvchilar

    def perform_create(self, serializer):
        listing = get_object_or_404(Listing, id=self.kwargs["listing_id"])  # ✅ Listing borligini tekshiramiz
        serializer.save(user=self.request.user, listing=listing)

# ✅ E’lon bo‘yicha barcha sharhlarni olish
class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]  # ✅ Hammaga ruxsat

    def get_queryset(self):
        listing = get_object_or_404(Listing, id=self.kwargs["listing_id"])  # ✅ Listing borligini tekshiramiz
        return Review.objects.filter(listing=listing)  # ✅ Shu e’longa tegishli sharhlarni qaytarish
