from django.shortcuts import render
from django.http import response, JsonResponse

def hello(request):
    data = {
        "Message": "Hi Hello Every one!!"
        }
    
    return JsonResponse(data)
