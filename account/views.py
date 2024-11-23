from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["POST",])
def log_out(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "You are log out "}, status=status.HTTP_200_OK)
    
    
