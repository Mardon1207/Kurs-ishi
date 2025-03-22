from django.urls import path
from .views import ReviewCreateView, ReviewListView

urlpatterns = [
    path("<int:listing_id>/reviews/", ReviewListView.as_view(), name="review-list"),
    path("<int:listing_id>/reviews/create/", ReviewCreateView.as_view(), name="review-create"),
]
