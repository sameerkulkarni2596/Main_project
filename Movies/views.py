from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Movies
from Movies.Serializer import MovieSerializer
from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def movieAPI(request, id=0):
    if request.method == 'GET':
        movies = Movies.objects.all()
        movies_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movies_serializer.data, safe=False)

    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to add the data", safe=False)
