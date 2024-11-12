from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def blog_list(request):
    if request.method == 'GET':
        all_blog = Blog.objects.filter(is_public = True)
        serializer = BlogSerializsers(all_blog, many=True)
        return Response(serializer.data) 
    
    if request.method == "POST":
        serializer = BlogSerializsers(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        

@api_view(['GET'])
def blog_detials(request,pk):
    blog = Blog.objects.get(is_public = True, pk=pk)
    serializer = BlogSerializsers(blog)

    return Response(serializer.data)
 

