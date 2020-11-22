from rest_framework.permissions import AllowAny, IsAuthenticated# IsAdminUser, 
from . serializers import MailSerailizer, RatingSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from . models import Mail, Rating


class CreateMail(CreateAPIView):
    serializer_class = MailSerailizer
    permission_classes = [AllowAny]
    


class AddRating(CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [AllowAny]

class RatingsList(ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()

class MessagesList(ListAPIView):
    serializer_class = MailSerailizer
    permission_classes = [IsAuthenticated]
    queryset = Mail.objects.all()


