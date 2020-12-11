from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import  viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import string
import random
from . serializers import (ItemSerializer, OrderItemSerializer, OrderSerializer, CategoriesSerializer,
                WishListSerializer, CouponSerializer, AddCouponSerializer, PaymentSerializer, ReviewSerializer)
from . models import (Item, Categories, OrderItem, Order,
            WishList, Coupon, Payment, Review)
        

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        item = get_object_or_404(self.queryset, slug=slug)
        item.views += 1
        item.save()
        return super().retrieve(request, slug)
        
    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    

    # def get_permissions(self):
    # # """
    # # Instantiates and returns the list of permissions that this view requires.
    # # """
    #     if self.action == 'list':
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        order_qs = Order.objects.filter(ordered=False, user= self.request.user)
        if order_qs:
            order = order_qs[0]
            # coupon = order.coupon
            if order.items.count() == 0:
                if order.coupon:
                    order.coupon = None
                    order.save()
                    print(order.coupon)
        return super().list(request, *args, **kwargs)

    


@permission_classes([IsAuthenticated])
@api_view(['POST', ])
def add_to_cart(request, slug):
    data = {}
    item = get_object_or_404(Item, slug=slug)
    #create order item
    order_item, created = OrderItem.objects.get_or_create(user = request.user, 
        item = item,
        is_ordered=False)
    # order_item.save()
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # check if user has active order
    if order_qs.exists():
        order = order_qs[0] # get latest order
        # check if item already exist in cart
        if order.items.filter(item__slug=item.slug).exists():
            data['message'] = f'{item.title} was already added to your cart.'
            data['type'] = 'info'
            print(f'{item.title} was already added to your cart.')
            return Response(data)
        else:
            order.items.add(order_item)
            data['message'] = f'{item.title} was added to your cart.'
            data['type'] = 'success'
            print(f'{item.title} was added to your cart.')
            return Response(data)
    else:
        # when user doesn't have active order
        # create new order
        date_now = timezone.now()
        order = Order.objects.create(user= request.user, start_date=date_now)
        order.items.add(order_item)
        data['message'] = f"{item.title} was added to your cart."
        data['type'] = 'success'
        print(f'{item.title} was added to your cart.')
        return Response(data)

@permission_classes([IsAuthenticated])
@api_view(['POST', ])
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user = request.user,
         ordered=False)
    # check if user has active item in cart
    data = {}
    if order_qs.exists():
        order = order_qs[0]
        # check if item was in cart
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(user=request.user,
            is_ordered=False,
            item = item)[0]
            order.items.remove(order_item)
            data['message'] = f"{item.title} was remove from your cart."
            data['type'] = 'success'
            return Response(data)
        # elif order.items.count() == 0:
        #     order.coupon.delete()
        # if item was not in cart
        else:
            data['message'] = f'{item.title} was not in your cart.'
            data['type'] = 'error'
            return Response(data)
    # if user had no active item in cart
    else:
        data['message'] = "You don't have an active order."
        data['type'] = 'info'
        return Response(data)
    
def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        print(coupon)
        return coupon
    except ObjectDoesNotExist:
        data = {}
        data['message'] = 'This coupon does not exist.'
        return Response(data)

class AddCouponView(APIView):
    serializer_class = AddCouponSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
            try:
                order = Order.objects.filter(user= request.user, ordered=False)[0]
                coupon_code = serializer.data
                order.coupon = get_coupon(self.request, coupon_code.get('code'))
                order.save()
                data['message'] = "Successfully added coupon"
                return Response(data)
                
            except ObjectDoesNotExist:
                data['message'] = "You don't have an active order."
                return Response(data)

            except ValueError:  
                data['message'] = 'This coupon does not exist'
                return Response(data)

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

class PaymentView(APIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        payment = Payment.objects
        serializer = self.serializer_class(payment, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
