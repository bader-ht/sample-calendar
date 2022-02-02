from rest_framework import response, status, views, exceptions
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from apps.customapi.serializers.custom import *
from apps.customapi.permissions import *
from apps.customapi.models import *

class CalendarCreateAPIView(generics.CreateAPIView):
    # Permission class to ensure user is logged in to access this view
    permission_classes = [IsAuthenticated] 
    serializer_class = CalendarSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        if self.request.user.is_authenticated:
            data["user"] = self.request.user.id
            # data["email"] = None

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

class CalendarRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsMyAccount]
    serializer_class = CalendarSerializer


class CalendarRetrieveUpdateAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsMyAccount]
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()

class CalendarDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsMyAccount]
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()

