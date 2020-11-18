from django.shortcuts import render
from . serializers import PageVisitSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

class CountPageVisit(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PageVisitSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PageVisitList(ListAPIView):
    serializer_class = PageVisitSerializer
    permission_classes = [IsAdminUser, ]