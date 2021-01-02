from django.contrib import admin
from .models import (Item, OrderItem, Order, Coupon, Categories,
        Payment, Review, WishList
#Payment
#UserProfile
#Address
)

def make_refund_accepted(ModelAdmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)

make_refund_accepted.short_description = 'Update orders to refund granted'

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'discount_price', 'is_free', 'item_type', 'downloads','views',)
    prepopulated_fields = {'slug': ('title',)} # new

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','slug',)
    prepopulated_fields = {'slug': ('category_name',)} # new

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    #'being_delivered',
                    #'received',
                    'refund_requested',
                    'refund_granted',
                    #'shipping_address',
                    #'billing_address',
                   # 'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        #'shipping_address',
        #'billing_address',
        #'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                  # 'being_delivered',
                  # 'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


# class AddressAdmin(admin.ModelAdmin):
#     list_display = ['user', 'street_address', 'apartment_address', 'country', 'zip', 'address_type', 'default']


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Categories, CategoryAdmin)
#admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)      
admin.site.register(Review)  
admin.site.register(WishList)
#admin.site.register(UserProfile)   

admin.site.site_header= 'eMav Admin'