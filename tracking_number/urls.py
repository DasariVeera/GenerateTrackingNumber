from django.urls import path

from .views import TrackingNumberAPIView

urlpatterns = [
    path('next-tracking-number/', TrackingNumberAPIView.as_view(), name="next-number")
]
