from rest_framework import serializers
from users.models import User
from . models import (Item, Categories, OrderItem, Order, WishList
            , Coupon, Review)
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class UserReviews(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'image',)

class ReviewSerializer(serializers.ModelSerializer):
    user = UserReviews(many=False, read_only=False)
    class Meta:
        model = Review
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'

class ItemSerializer(TaggitSerializer, serializers.ModelSerializer):
    total_reviews       = serializers.IntegerField(source='get_total_reviews', read_only=True)
    computed_review     = serializers.IntegerField(source='get_computed_reviews', read_only=True)
    file_name           = serializers.CharField(source='get_file_name', read_only=True)
    item_price          = serializers.IntegerField(source = 'get_price', read_only=True)
    reviews             = ReviewSerializer(many=True, read_only=True)
    category            = CategoriesSerializer(many=False, read_only=True)
    tags = TagListSerializerField()

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

        representation['item_size'] = size
        representation["item_name"] = instance.get_file_name()
        representation["download_url"] = instance.get_file_name()
        return representation

    def validate_title(self, value):
        qs = Item.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
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
    sub_total = serializers.IntegerField(source='get_sub_total', read_only=True)
    sub_total_selected_items = serializers.IntegerField(source='get_selected_items_sub_total', read_only=True)
    total = serializers.IntegerField(source='get_total', read_only=True)
    total_items = serializers.IntegerField(source='get_total_items', read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    total_items = serializers.IntegerField(source = 'get_total_items', read_only=True)
    
    class Meta:
        model = WishList
        fields = '__all__'

class AddCouponSerializer(serializers.Serializer):
    code = serializers.CharField(max_length = 100) 
