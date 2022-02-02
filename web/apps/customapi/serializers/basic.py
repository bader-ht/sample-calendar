from apps.customapi.models import *
from rest_framework import serializers

class CalendarSerializer(serializers.ModelSerializer):

	class Meta:
		model = Calendar
		fields = '__all__' 


	def validate(self, attrs):
		'''
		Overridden to include checking of schedules (per user) to prevent overlapping timmings
		'''
		attrs = super().validate(attrs)
		user = attrs.get("user")
		start = attrs.get("start_date")
		end = attrs.get("end_date")
		
		query = Q(user=user) & ( Q(start_date__lte=start) & Q(end_date__gt=start) | \
			 Q(start_date__lt=end) & Q(end_date__gte=end) | \
			 Q(start_date__gte=end) & Q(end_date__lte=end))
		
		queryset = Calendar.objects.filter(query)

		if queryset.exists():
			raise ValidationError("The time you added conflicts with your existing schedule")
		
		return attrs


class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = '__all__' 


	def validate(self, attrs):
		'''
		Overridden to include checking of schedules (per user) to prevent overlapping timmings
		'''
		attrs = super().validate(attrs)
		calendar = attrs.get("calendar")  
		user = calendar.user
		start = attrs.get("start_date")
		end = attrs.get("end_date")
		
		if not (start >= calendar.start_date and end <= calendar.end_date):
			raise ValidationError("The time you are attempting to book is not valid.")

		query = Q(user=user) & ( Q(start_date__lte=start) & Q(end_date__gt=start) | \
			 Q(start_date__lt=end) & Q(end_date__gte=end) | \
			 Q(start_date__gte=end) & Q(end_date__lte=end))
		
		queryset = Reservation.objects.filter(query)

		if queryset.exists():
			raise ValidationError("This time slot has already been booked.")
		
		return attrs


