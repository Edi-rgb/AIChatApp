from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def front_page(request):
    return render(request, 'front_page.html')