from django.urls import path, include
from .views import StripeCheckoutView, StripeWebhookView

urlpatterns = [
    path('checkout',StripeCheckoutView.as_view(), name="checkout"),
    path('stripe-webhook/', StripeWebhookView.as_view(), name='stripe-webhook'),
]