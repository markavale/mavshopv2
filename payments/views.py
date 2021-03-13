from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status#,viewsets
from . serializers import PaymentSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from . models import Payment
from django.conf import settings
from core.utils import get_order_instance
# from core.models import Order
import stripe

stripe_keys = {
    'secret_key': settings.STRIPE_API_SK,
    'publishable_key': settings.STRIPE_API_PB,
}

stripe.api_key =  stripe_keys['secret_key']

@permission_classes([IsAdminUser])
@api_view(['POST',])
def create_checkout_session(request):
    data = {}
    try:
        order_instance = get_order_instance(request, request.user, False)
        # checkout_session = stripe.checkout.Session.create(
        # success_url="https://example.com/success",
        # cancel_url="https://example.com/cancel",
        # payment_method_types=["card"],
        # line_items=[
        #     {
        #     "price": "price_H5ggYwtDq4fbrJ",
        #     "quantity": 1,
        #     },
        # ],
        # mode="payment",
        # )
        # checkout_session =  stripe.Charge.create(
        #                 amount=1000,  # cents
        #                 currency="usd",
        #                 customer="markvawe"
        #             )
        checkout_session =  stripe.checkout.Session.create(
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
        payment_method_types=["card"],
        # customer = order_instance.user.email,
        line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        # 'unit_amount_subtotal': int(order_instance.get_selected_items_sub_total()),
                        'unit_amount': int(order_instance.get_total()),
                        'product_data': {
                            'name': 'Tet from backend',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    # 'quantity': 1,
                },
            ],
        mode="payment",
        )
        data = checkout_session
        
    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught

        print('Status is: %s' % e.http_status)
        print('Code is: %s' % e.code)
        # param is '' in this case
        print('Param is: %s' % e.param)
        print('Message is: %s' % e.user_message)
    except stripe.error.RateLimitError as e:
        data['error'] = "RateLimitError"
        # Too many requests made to the API too quickly
        
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        data['error'] = "InvalidRequestError"
    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        data['error'] = "AuthenticationError"
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        data['error'] = "APIConnectionError"
    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        data['error'] = "StripeError"
    except Exception as e:
        # Something else happened, completely unrelated to Stripe
        data['error'] = "Error"
    return Response(data)
    # test_payment_intent = stripe.PaymentIntent.create(
    # amount=1000, currency='usd', 
    # payment_method_types=['card'],
    # receipt_email='markavale1@gmail.com')
    # return Response(status=status.HTTP_200_OK, data=test_payment_intent)

@api_view(['POST'])
def save_stripe_info(request):
    data = request.data
    email = data['email']
    payment_method_id = data['payment_method_id']
    extra_msg = '' # add new variable to response message
    # checking if customer with provided email already exists
    customer_data = stripe.Customer.list(email=email).data   

    # if the array is empty it means the email has not been used yet  
    if len(customer_data) == 0:
    # creating customer
        customer = stripe.Customer.create(
        email=email, payment_method=payment_method_id)
        
    else:
        customer = customer_data[0]
        extra_msg = "Customer already existed."
        stripe.PaymentIntent.create(
        customer=customer, 
        payment_method=payment_method_id,  
        currency='pln', # you can provide any currency you want
        amount=999,     # it equals 9.99 PLN
        confirm=True)     

    return Response(status=status.HTTP_200_OK, 
    data={'message': 'Success', 'data': {
        'customer_id': customer.id, 'extra_msg': extra_msg}
    })

class PaymentView(APIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        payment = Payment.objects.all()
        serializer = self.serializer_class(payment, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()