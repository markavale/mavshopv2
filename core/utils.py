from django.http.response import Http404
from rest_framework.response import Response
from .models import Order, Item
import string
import random

# DRY: get request use order
def get_user_orders(request, user, ordered):
    order_qs = Order.objects.filter(user=user, ordered=ordered)
    return order_qs

def get_item_instance(request, slug):
    try:
        instace = Item.objects.get(slug=slug)
        return instace
    except Item.DoesNotExist:
        return Http404

def get_order_instance(request, user, ordered):
    try:
        order = Order.objects.filter(user = user, ordered=ordered)
        if order.exists():
            return order[0]
        return []
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'})

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
