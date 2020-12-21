# from django.db.models.fields import CharField
from rest_framework import serializers
import os
from users.models import User
# from django.conf import 
from . models import (Item, Categories, OrderItem, Order,
            WishList, Coupon, Payment, Review)

class UserReviews(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'image',)

class ReviewSerializer(serializers.ModelSerializer):
    user = UserReviews(many=False, read_only=False)
    class Meta:
        model = Review
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    total_reviews       = serializers.IntegerField(source='get_total_reviews', read_only=True)
    computed_review     = serializers.IntegerField(source='get_computed_reviews', read_only=True)
    file_name           = serializers.CharField(source='get_file_name', read_only=True)
    reviews             = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        size_byte = instance.download_file.size
        size_kb = round(instance.download_file.size / 1024, 2)
        size_mb = round(instance.download_file.size / (1024 * 1024), 2)
        size_gb = round(instance.download_file.size / (1024 * 1024 * 1024), 2)
        size = 0
        # condition for returning a proper size of file
        if size_gb >= 0.50:
            size = str(size_gb) + "Gb"
        elif size_mb >= 0.50:
            size = str(size_mb) + "Mb"
        elif size_kb >= 0.50:
            size = str(size_kb) + "Kb"
        else:
            size = str(size_byte) + "Byte"
        
        file = {
            # "size_byte": size_byte,
            # "size_kb": size_kb,
            # "size_mb": size_mb,
            # "size_gb": size_gb,
            "size": size,
            "name": instance.get_file_name(), # referring to class method in models.py
            "download_url": instance.get_download_url()
        }
        representation['file'] = file
        return representation

class OrderItemSerializer(serializers.ModelSerializer):
    # item = serializers.CharField(read_only=True)
    item = ItemSerializer(many=False, read_only=False)

    class Meta:
        model = OrderItem
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=False)
    coupon = CouponSerializer(many=False, read_only=True)
    sub_total = serializers.CharField(source='get_sub_total', read_only=True)
    total = serializers.CharField(source='get_total', read_only=True)
    total_items = serializers.CharField(source='get_total_items', read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'



class AddCouponSerializer(serializers.Serializer):
    code = serializers.CharField(max_length = 100) 
