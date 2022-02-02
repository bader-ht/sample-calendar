from statistics import mode
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models import Q

from django.core.exceptions import ValidationError

class Calendar(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	interval = models.IntegerField(default=15, choices=((15, "15"), (30, "30"), (45,"45")))
	user = models.ForeignKey('auth.User', related_name='calendar', on_delete=models.CASCADE)


class Reservation(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=255)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	user=models.ForeignKey('auth.User', related_name='reservation', on_delete=models.CASCADE)
	calendar=models.ForeignKey('customapi.Calendar', related_name='reservation', on_delete=models.CASCADE)
