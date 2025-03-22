from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from .models import Listing
from .serializers import ListingSerializer
from django_filters.rest_framework import DjangoFilterBackend

# ✅ E‘lon yaratish
class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# ✅ Barcha e’lonlarni ko‘rish + 🔍 Kategoriya bo‘yicha filter
class ListingListView(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']  # 🔹 Kategoriyaga qarab filtrlash

    def get_queryset(self):
        return Listing.objects.all()

# ✅ Faqat bitta e’lonni ko‘rish
class ListingDetailView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]

# ✅ E‘lonni o‘zgartirish (faqat egasi tahrir qila oladi)
class ListingUpdateView(generics.UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        listing = self.get_object()
        if listing.owner != self.request.user:
            raise PermissionDenied("Siz faqat o‘z e‘loningizni tahrir qila olasiz.")
        serializer.save()

# ✅ E‘lonni o‘chirish (faqat egasi o‘chira oladi)
class ListingDeleteView(generics.DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("Siz faqat o‘z e‘loningizni o‘chira olasiz.")
        instance.delete()
