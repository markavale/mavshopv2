from django.urls import path
from . views import CreateMail, AddRating

urlpatterns = [
    path('send-mail/', CreateMail.as_view(), name='send-mail'),
    path('add-rating/', AddRating.as_view(), name='rating'),
]
