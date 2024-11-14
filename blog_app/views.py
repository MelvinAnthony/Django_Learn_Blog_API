from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class CategoryListViews(APIView):
    def get(self,request):
        all_category = Category.objects.all()
        serializer = CategorySerializer(all_category, many = True)
        return Response(serializer.data)
    
class CategoryDetialViews(APIView):
    def get(self,request, pk):
        single_category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(single_category)
        return Response(serializer.data)

# GET, POST -> method work here
class BlogListView(APIView):
    def get(self,request):
        all_blog = Blog.objects.filter(is_public = True)
        serializer = BlogSerializer(all_blog, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    def post(self,request):
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
# GET, PUT, DELETE
class BlogDetialsView(APIView):
    def get(self, request, pk):
        blog = Blog.objects.get(is_public = True, pk=pk)
        serializer = BlogSerializer(blog)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        blog = Blog.objects.get(is_public = True, pk=pk)
        serializer = BlogSerializer(blog,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

    def delete(self,request,pk):
        blog = Blog.objects.get(is_public = True,pk=pk)
        blog.delete()
        return Response("Data Delete Sucessfully", status=status.HTTP_200_OK)


'''
@api_view(['GET','POST'])
def blog_list(request):
    if request.method == 'GET':
        all_blog = Blog.objects.filter(is_public = True)
        serializer = BlogSerializsers(all_blog, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    if request.method == "POST":
        serializer = BlogSerializsers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def blog_detials(request,pk):
    if request.method == 'GET':
        blog = Blog.objects.get(is_public = True, pk=pk)
        serializer = BlogSerializsers(blog)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        blog = Blog.objects.get(is_public = True, pk=pk)
        serializer = BlogSerializsers(blog,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        blog = Blog.objects.get(is_public = True,pk=pk)
        blog.delete()
        return Response("Data Delete Sucessfully", status=status.HTTP_200_OK)

'''