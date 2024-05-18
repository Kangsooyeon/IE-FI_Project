import csv
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Location
from .serializers import LocationSerializer
import os
from django.conf import settings



# Create your views here.
def save_location(request):
    file_path = os.path.join(settings.BASE_DIR, 'map/data/data_grouped.csv')
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  
        for row in reader:
            location_data = {
                'province': row[0],
                'city': row[1],
                'region': row[2],
                'latitude': float(row[3]),
                'longitude': float(row[4]),
            }
            serializer = LocationSerializer(data=location_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(serializer.errors, status=400)
    return HttpResponse('Data saved successfully', status=200)


@api_view(['GET'])
def get_location(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)
