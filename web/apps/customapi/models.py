from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models import Q

from django.core.exceptions import ValidationError

class Calendar(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	interval = models.IntegerField(default=15)
	user = models.ForeignKey('auth.User', related_name='calendar', on_delete=models.CASCADE)