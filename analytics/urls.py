from django.urls import path
from . views import CountPageVisit, PageVisitList

urlpatterns = [
    path('count-visit/', CountPageVisit.as_view(), name='page-visit'),
    path('page-views/', PageVisitList.as_view(), name='page-views'),
]
