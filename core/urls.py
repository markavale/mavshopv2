from django.urls import path#, include
from core.views.user import (ItemViewSet, OrderItemViewSet, OrdersViewSet, add_to_cart,
            remove_from_cart, AddCouponView, CouponViewSet, ReviewViewSet,
            download_view, CatergoryView, WishListView, wish_list_add_or_remove,
            apply_coupon, remove_coupon, remove_selected_items, invert_order_items_select_status,
            invert_use_coupon_from_order,
            
            
            )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', ItemViewSet),
router.register('order-items', OrderItemViewSet, basename='OrderItem'),
router.register('orders', OrdersViewSet, basename='Order'),
router.register('coupons', CouponViewSet),
router.register('reviews', ReviewViewSet),

urlpatterns = [
    # path('checkout/',  CheckOutView.as_view(), name='checkout'),
    # path('payment/<payment_option>/',  PaymentView.as_view(), name='payment'),
    # path('product/<slug>/',  ItemDetailView.as_view(), name='product'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    # path('order-items/<id>/detail/', OrderItemDetail.as_view(), name='order-item-detail'),
    # path('order-items/<id>/update/', OrderItemUpdate.as_view(), name='order-item-update'),
    path('items/categories/', CatergoryView.as_view(), name='category'),
    path('items/<slug>/download/', download_view, name="download-file"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-selected-items/', remove_selected_items, name='remove-selected-items'),
    path('invert-selected-items/', invert_order_items_select_status, name='invert-select-items'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('wish-list/<slug>/', wish_list_add_or_remove, name='wish-list'),
    path('wish-list/', WishListView.as_view(), name='user-wish'),
    path('coupons/<id>/apply/', apply_coupon, name='apply-coupon'),
    path('coupons/remove/', remove_coupon, name='apply-coupon'),
    path('invert-order-use-coupon/', invert_use_coupon_from_order, name='order-use-coupon')
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]

urlpatterns += router.urls