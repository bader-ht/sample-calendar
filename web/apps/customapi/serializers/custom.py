from apps.customapi.models import *
from rest_framework import serializers

class CalendarSerializer(serializers.ModelSerializer):
	# email = serializers.EmailField(required=False)

	class Meta:
		model = Calendar
		fields = '__all__' 



