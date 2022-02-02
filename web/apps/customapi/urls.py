from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from apps.customapi.views.basic import *
router = routers.DefaultRouter()

urlpatterns = [
    path("accounts/", include("dj_rest_auth.urls")),
    path("calendar/create/", CalendarCreateAPIView.as_view(), name="calendar-create"),
    path("calendar/edit/", CalendarRetrieveUpdateAPIView.as_view(), name="calendar-edit"),
    path("calendar/list/", CalendarRetrieveUpdateAPIView.as_view(), name="calendar-edit"),
    path("calendar/delete/", CalendarRetrieveUpdateAPIView.as_view(), name="calendar-edit"),
]
