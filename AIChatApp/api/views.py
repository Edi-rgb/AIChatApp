from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

from .SugestiiAI.pre_procesare import process

# # metoda 1
# def index(request):
#     json_response = json.dumps({"message":"This is the root URL of our API"})
#     return HttpResponse(json_response,status=200)

# metoda 2
def index(request):
    json_response = {"message":"This is the root URL of our API"}
    return JsonResponse(json_response)

def suggestions(request):
    input = request.GET.get('text',None)

    if not input:
        return JsonResponse({"message":"text query parameter is missing"})
    else:
        return JsonResponse({"output":process(input)})
        