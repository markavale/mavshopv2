from django.urls import path
from . views import CountPageVisit

urlpatterns = [
    path('count-visit/', CountPageVisit.as_view(), name='page-visit'),
]
