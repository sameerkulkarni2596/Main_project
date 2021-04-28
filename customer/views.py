from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import customer
from customer.Serializer import customerSerializer,customercredSerializer
from django.core.files.storage import default_storage
# Create your views here.

# Create your views here.

@csrf_exempt
def customerApi(request,id=0):
     if request.method=='GET':
         customers = customer.objects.all()
         customers_serializer = customerSerializer(customers,many=True)
         return JsonResponse(customers_serializer.data,safe=False)
     elif request.method =='POST':
        customers_data=JSONParser().parse(request)
        customers_serializer = customerSerializer(data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Added Successfully!!" , safe = True)
        return JsonResponse("Failed to Add ", safe = False)


@csrf_exempt
def customercredApi(request):
    if request.method == 'GET':
        customercreds = customer.objects.all()
        customercreds_serializer = customercredSerializer(customercreds, many=True)
        return JsonResponse(customercreds_serializer.data, safe=False)

    elif request.method == 'POST':
        customercred_data = JSONParser().parse(request)
        customercred_serializer = customercredSerializer(data=customercred_data)
        if customercred_serializer.is_valid():
            customercred_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to add the data", safe=False)
