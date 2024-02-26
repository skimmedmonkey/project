from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DateData

# Create your views here.
class CompareDates(APIView):
    def post(self, request):
        """Reads JSON data from request"""
        try:
            data  = request.data
        except Exception as e:
            return Response({'error': 'Failed to read JSON data'}, status=400)
        
        serializer = DateData(data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        data1 = [item.dict() for item in serializer.validated_data if item['source'] == 'array1']
        data2 = [item.dict() for item in serializer.validated_data if item['source'] == 'array2']

        if not data1 or not data2:
            return Response({'error': 'Both arrays cannot be empty'}, status=400)

        # Compare data and find discrepancies
        discrepancies = []
        for row1 in data1:
            for row2 in data2:
                if row1['name'] == row2['name'] and row1['date'] != row2['date']:
                    discrepancies.append({'name': row1['name'], 'date': row1['date']})
                    break  # Stop comparing if a match is found for the name

        # Return JSON with discrepancies
        return Response(discrepancies)