from django.urls import path

from .views import CustomerDealsAPIView

urlpatterns = [
    path('customerdeals/', CustomerDealsAPIView.as_view())
]
