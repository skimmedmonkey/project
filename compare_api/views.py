from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import NameDate
from .serializers import NameDateSerializer

class CompareNamesDatesView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        # Deserialize the JSON data
        data = request.data

        # Validate and save the data for array1
        serializer_array1 = NameDateSerializer(data=data.get('array1', []), many=True)
        if serializer_array1.is_valid():
            serializer_array1.save()

        # Validate and save the data for array2
        serializer_array2 = NameDateSerializer(data=data.get('array2', []), many=True)
        if serializer_array2.is_valid():
            serializer_array2.save()

        # Compare names and dates
        result = []

        # Iterate over array2
        for name_date_array2 in serializer_array2.validated_data:
            name_array2 = name_date_array2['name']
            date_array2 = name_date_array2['date']

            # Check if the name exists in array1 and the dates are different
            matching_dates_array1 = NameDate.objects.filter(name=name_array2)
            found_difference = False

            for matching_date_array1 in matching_dates_array1:
                if matching_date_array1.date != date_array2:
                    found_difference = True
                    break  # Break the loop as soon as a difference is found

            # Include the name and date from array2 only if a difference is found
            if found_difference:
                result.append({
                    'name': name_array2,
                    'date_array2': date_array2
                })

        # Return the result
        return Response(result)