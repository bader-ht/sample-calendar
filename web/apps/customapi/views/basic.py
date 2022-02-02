from rest_framework import response, status, views, exceptions
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from apps.customapi.serializers.custom import *

class CalendarCreateAPIView(generics.CreateAPIView):
    serializer_class = CalendarSerializer

class CalendarRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):

    serializer_class = CalendarSerializer


class CalendarDeleteAPIView(generics.ListAPIView):
    serializer_class = CalendarSerializer

class CalendarDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CalendarSerializer
