from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

# # metoda 1
# def index(request):
#     json_response = json.dumps({"message":"This is the root URL of our API"})
#     return HttpResponse(json_response,status=200)

# metoda 2
def index(request):
    json_response = {"message":"This is the root URL of our API"}
    return JsonResponse(json_response)

