from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ListingCreateView, ListingListView, ListingDetailView,
    ListingUpdateView, ListingDeleteView
)

urlpatterns = [
    path('', ListingListView.as_view(), name='listing-list'),
    path('create/', ListingCreateView.as_view(), name='listing-create'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('<int:pk>/update/', ListingUpdateView.as_view(), name='listing-update'),
    path('<int:pk>/delete/', ListingDeleteView.as_view(), name='listing-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)