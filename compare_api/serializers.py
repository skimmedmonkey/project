from rest_framework import serializers

class DateData(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()