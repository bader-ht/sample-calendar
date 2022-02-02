from rest_framework import response, status, views, exceptions
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from apps.customapi.serializers.basic import *
from apps.customapi.permissions import *
from apps.customapi.models import *
from django.db.models import Q
from django.utils import timezone
import datetime

class CalendarCreateAPIView(generics.CreateAPIView):
    # Permission class to ensure user is logged in to access this view
    permission_classes = [IsAuthenticated] 
    serializer_class = CalendarSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        if self.request.user.is_authenticated:
            data["user"] = self.request.user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

class CalendarRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    # Permission class to ensure user is logged in to access this view
    permission_classes = [IsAuthenticated, IsMyAccount]
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()


class CalendarListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CalendarSerializer
    # Queryset can be updated to return only the calender items of the requester.
    queryset = Calendar.objects.all()
    

class CalendarDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsMyAccount]
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()


class ReservationCreateAPIView(generics.CreateAPIView):
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        start = timezone.datetime.strptime(data['start_date'], "%d-%m-%Y %H:%M:%S:%Z")

        
        cal = Calendar.objects.get(id=data['calendar'])
        data['user'] = cal.user.id
        data['end_date'] = start + datetime.timedelta(minutes=cal.interval)


        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

