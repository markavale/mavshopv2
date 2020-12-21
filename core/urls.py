from django.urls import path#, include
from . views import (ItemViewSet, OrderItemViewSet, OrdersViewSet, add_to_cart,
            remove_from_cart, AddCouponView, CouponViewSet, PaymentView, ReviewViewSet,
            download_view)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', ItemViewSet),
router.register('order-items', OrderItemViewSet),
router.register('orders', OrdersViewSet),
router.register('coupons', CouponViewSet),
router.register('reviews', ReviewViewSet)

urlpatterns = [
    # path('checkout/',  CheckOutView.as_view(), name='checkout'),
    # path('payment/<payment_option>/',  PaymentView.as_view(), name='payment'),
    # path('product/<slug>/',  ItemDetailView.as_view(), name='product'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('items/<slug>/download/', download_view, name="download-file"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('payment/', PaymentView.as_view(), name='payment'),
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]

urlpatterns += router.urls