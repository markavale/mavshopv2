from django.urls import path
from . views import CreateMail, AddRating, RatingsList, MessagesList

urlpatterns = [
    path('send-mail/', CreateMail.as_view(), name='send-mail'),
    path('add-rating/', AddRating.as_view(), name='create-rating'),
    path('ratings/', RatingsList.as_view(), name='ratings'),
    path('messages/', MessagesList.as_view(), name='messages'),
]
