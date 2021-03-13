from django.urls import path
from . views import PaymentView, create_checkout_session

urlpatterns = [
    path('payments/', PaymentView.as_view(), name='payments'),
    path('payments/stripe-charge/', create_checkout_session, name='test-payment'),
]
