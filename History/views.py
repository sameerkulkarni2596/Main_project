from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import History
from History.Serializer import HistorySerializer
from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def historyAPI(request, id=0):
    if request.method == 'GET':
        history = History.objects.all()
        history_serializer = HistorySerializer(history, many=True)
        return JsonResponse(history_serializer.data, safe=False)

    elif request.method == 'POST':
        history_data = JSONParser().parse(request)
        history_serializer = HistorySerializer(data=history_data)
        if history_serializer.is_valid():
            history_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to add the data", safe=False)



