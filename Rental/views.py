from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Rentals
from Rental.Serializer import RentalSerializer
from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def rentalAPI(request, id=0):
    if request.method == 'GET':
        rentals = Rentals.objects.all()
        rentals_serializer = RentalSerializer(rentals, many=True)
        return JsonResponse(rentals_serializer.data, safe=False)

    elif request.method == 'POST':
        rental_data = JSONParser().parse(request)
        rental_serializer = RentalSerializer(data=rental_data)
        if rental_serializer.is_valid():
            rental_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to add the data", safe=False)
