from rest_framework import serializers
from .models import NameDate

class NameDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameDate
        fields = ['name', 'date']