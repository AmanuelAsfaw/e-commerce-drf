from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def getRoutes(request):
    return JsonResponse('Hello', safe=False)