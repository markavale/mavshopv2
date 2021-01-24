from django.db.models import query
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import  viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import string
import random
from core.serializers import (ItemSerializer, OrderItemSerializer, OrderSerializer, CategoriesSerializer,
                 CouponSerializer, AddCouponSerializer, PaymentSerializer, ReviewSerializer, WishListSerializer,
                 WishRetrieveSerializer,)
from core.models import (Item, Categories, OrderItem, Order,
             Coupon, Payment, Review, WishList)
# import os
# from django.conf import settings
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# DRY: get request use order
def get_user_orders(request, user, ordered):
    order_qs = Order.objects.filter(user=user, ordered=ordered)
    return order_qs


# @permission_classes([AllowAny])
# @api_view(['GET', ])
def download_view(request, slug):
    item = Item.objects.get(slug=slug)
    filename = item.get_file_name()
    # if request.method == "GET":
    if item.is_free:
        response = HttpResponse(item.download_file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        item.downloads += 1
        item.save()
        return response
        # return Response(response)
        # else:
        #     response = HttpResponse(item.download_file, content_type='text/plain')
        #     response['Content-Disposition'] = 'attachment; filename=%s' % filename
        #     item.downloads += 1
        #     item.save()
        #     return response   

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

class CatergoryView(ListAPIView):
    queryset = Categories.objects.all().order_by('category_name')
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category_type']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-timestamp')
    serializer_class = ItemSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['item_type', 'is_free', 'category']
    search_fields = ['title', 'tags__name']

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
    serializer_class = OrderItemSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = OrderItem.objects.filter(user = self.request.user)
        return queryset
    

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
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        # order_qs = Order.objects.filter(ordered=False, user= self.request.user)
        # if order_qs:
        #     order = order_qs[0]
        #     # coupon = order.coupon
        #     if order.items.count() == 0:
        #         if order.coupon:
        #             order.coupon = None
        #             order.save()
        #             print(order.coupon)
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated] # AllowAny
        elif self.action == 'create':
            permission_classes = [AllowAny] # AllowAny
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


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
            data['color'] = 'blue'
            print(f'{item.title} was already added to your cart.')
            return Response(data)
        else:
            order.items.add(order_item)
            data['message'] = f'{item.title} was added to your cart.'
            data['type'] = 'success'
            data['color'] = 'green'
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

@permission_classes([IsAuthenticated])
@api_view(['POST', ])
def apply_coupon(request, id):
    try:
        coupon = Coupon.objects.get(id=id)
        order_qs = get_user_orders(request, user=request.user, ordered=False)
        data = {}
        if order_qs.exists():
            order = order_qs[0]
            order.add_coupon(coupon)
            data['message'] = "Coupon applied"
            return Response(data)
        
    except Coupon.DoesNotExist:
        return Response({'message': 'Coupon does not exist.'}, status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])
@api_view(['POST', ])
def remove_coupon(request):
    try:
        order_qs = get_user_orders(request, user=request.user, ordered=False)
        data = {}
        if order_qs.exists():
            order = order_qs[0]
            order.remove_coupon()
            data['message'] = "Coupon was successfully removed."
            return Response(data)
        else:
            data['message'] = "You don't have active coupon."
            return Response(data)

    except Coupon.DoesNotExist:
        return Response({'message': 'Coupon does not exist.'}, status=status.HTTP_404_NOT_FOUND)    

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
        payment = Payment.objects.all()
        serializer = self.serializer_class(payment, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

class WishListView(ListAPIView):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all().order_by('-timestamp')
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        #queryset = self.filter_queryset(self.get_queryset())
        queryset = self.queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

@permission_classes([IsAuthenticated,])
@api_view(['POST', 'GET', ])
def wish_list_add_or_remove(request, slug):
    try:
        item = Item.objects.get(slug=slug)
        data = {}
        wish_qs = WishList.objects.filter(user=request.user).order_by('-timestamp')
    except Item.DoesNotExist:
        data = {}
        data['message'] = "Not found!!"
        return Response(data,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print(item)
        if wish_qs.exists():
            wish = wish_qs[0]
            wish_instance = wish.items.filter(slug = item.slug)
            if wish_instance.exists():
                data['isWish'] = True
                return Response(data)
            else:
                data['isWish'] = False
                return Response(data)
        else:
            data['isWish'] = False
            return Response(data)

    if request.method == "POST":
        # item = get_object_or_404(Item, slug=slug)
        # data = {}
        # wish_qs = WishList.objects.filter(user=request.user).order_by('-timestamp')
        print(wish_qs) 
        # check if user does have an active wish list
        if wish_qs.exists():
            print("Executed inside of wish_qs if exists")
            wish = wish_qs[0]
            # check if wish item already in wish 
            wish_obj = wish.items.filter(slug = item.slug)# if you define wish.items it means you're already have an access to the object itself
            print(wish_obj)
            if wish_obj.exists():
                # if true remove item that already in wish list
                wish.items.remove(item)
                data['message'] = f"{item.title} was remove from your wish list."
                print(f"{item.title} was remove from your wish list.")
                return Response(data)
            else:
                # else add item to wish list
                wish.items.add(item)
                data['message'] = f"{item.title} was added to your wish list."
                print(f"{item.title} was added to your wish list.")
                return Response(data)
        else:
            print("Executed inside in else statement for uncreated yet..")
            # else if user doesn't have active wish list create one
            date_now = timezone.now()
            wish = WishList.objects.create(user = request.user, timestamp = date_now)
            wish.items.add(item)
            wish.save()
            data['message'] = f"{item.title} was added to your wish list."
            print(f"{item.title} was added to your wish list.")
            return Response(data)

