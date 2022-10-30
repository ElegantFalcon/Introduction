from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt




# Create your views here.


def home(request) :
    return render(request, 'Hi.html')