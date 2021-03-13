from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import  viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from core.serializers import (ItemSerializer, OrderItemSerializer, OrderSerializer, CategoriesSerializer,
                 CouponSerializer, AddCouponSerializer, ReviewSerializer, WishListSerializer,
                        )
from core.models import (Item, Categories, OrderItem, Order,
             Coupon, Review, WishList)
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.permissions import IsAssigned
from core.utils import (get_user_orders, get_item_instance, get_order_instance, 
        create_ref_code
)

@permission_classes([AllowAny])
@api_view(['GET', ])
def download_view(request, slug):
    item = Item.objects.get(slug=slug)
    filename = item.get_file_name()
    if item.is_free:
        response = HttpResponse(item.download_file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        item.downloads += 1
        item.save()
        return response  

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
    permission_classes = [IsAssigned]

    def get_queryset(self):
        queryset = OrderItem.objects.filter(user = self.request.user, is_ordered=False).order_by('-item')
        return queryset

    def partial_update(self, request, *args, **kwargs):
        order_item = self.get_object()
        serializer = self.serializer_class(order_item, data= request.data, partial=True)
        item = get_item_instance(request, order_item.item.slug)
        data = {}
        
        if serializer.is_valid():
            for key, value in serializer.validated_data.items():
                print(key, value)
                serializer.validated_data[f'{key}'] = value
                serializer.save()
            data['success'] = "Update success"
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        order_item = self.get_object()
        serializer = self.serializer_class(order_item, data= request.data)
        item = get_item_instance(request, order_item.item.slug)
        data = {}
        
        if serializer.is_valid():
            for key, value in serializer.validated_data.items():
                serializer.validated_data[f'{key}'] = value
                serializer.save()
            data['success'] = "Update success"
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAssigned])
def invert_order_items_select_status(request):
    order = get_order_instance(request, request.user, False)
    order_items = order.items.all()
    data = {}
    print(order_items)
    if request.method == 'PATCH':
        print(request.data['is_selected'])
        for order_item in order_items:
            order_item.is_selected = request.data['is_selected']
            order_item.save()
        # serializer = OrderItemSerializer(order_items, data=request.data, partial=True)
        # if serializer.is_valid():
        #     for key, value in serializer.validated_data.items():
        #         print(key, value)
        #         serializer.validated_data[f'{key}'] = value
        #         serializer.save()
        data['success'] = "Update success"
        return Response(data)
        # return Response(status=status.HTTP_200_OK) 
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAssigned])
def invert_use_coupon_from_order(request):
    order = get_order_instance(request, request.user, False)
    data = {}
    if request.method == 'PATCH':
        print(request.data['use_coupon'])
        serializer = OrderItemSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['use_coupon'] = request.data['use_coupon']
            serializer.save()
        data['success'] = "Update success"
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    lookup_field = 'id'
    permission_classes = [IsAssigned]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, ordered=False)

    def partial_update(self, request, *args, **kwargs):
        order = get_order_instance(request, request.user, False)
        serializer = self.serializer_class(order, data= request.data, partial=True)
        data = {}
        
        if serializer.is_valid():
            for key, value in serializer.validated_data.items():
                print(key, value)
                serializer.validated_data[f'{key}'] = value
                serializer.save()
            data['success'] = "Update success"
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        order = get_order_instance(request, request.user, False)
        serializer = self.serializer_class(order, data= request.data)
        data = {}
        
        if serializer.is_valid():
            for key, value in serializer.validated_data.items():
                print(key, value)
                serializer.validated_data[f'{key}'] = value
                serializer.save()
            data['success'] = "Update success"
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAssigned])
@api_view(['POST', ])
def add_to_cart(request, slug):
    data = {}
    item = get_object_or_404(Item, slug=slug)
    #create order item
    order_item, created = OrderItem.objects.get_or_create(user = request.user, 
        item = item,
        is_ordered=False)
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

@permission_classes([IsAssigned])
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

@permission_classes([IsAssigned])
@api_view(['POST', ])
def remove_selected_items(request):
    data = {}
    try:
        order_items = OrderItem.objects.filter(user=request.user, is_ordered=False, is_selected=True)
        [order_item.delete() for order_item in order_items]
        total_item = 'items' if len(order_items) > 1 else 'item'
        data['success'] = f"{len(order_items)} {total_item} was deleted successfully"
        return Response(data, status=status.HTTP_200_OK)
    except OrderItem.DoesNotExist:
        data['error'] = "You do not have an active order"
        return Response(data, status=status.HTTP_404_NOT_FOUND)

def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        print(coupon)
        return coupon
    except Coupon.DoesNotExist:
        data = {}
        data['message'] = 'This coupon does not exist.'
        return Response(data)

@permission_classes([IsAssigned])
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

@permission_classes([IsAssigned])
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
                
            except Order.DoesNotExist:
                data['message'] = "You don't have an active order."
                return Response(data)

            except ValueError:  
                data['message'] = 'This coupon does not exist'
                return Response(data)

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'



class WishListView(ListAPIView):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all().order_by('-timestamp')
    permission_classes = [IsAssigned,]

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

@permission_classes([IsAssigned,])
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

