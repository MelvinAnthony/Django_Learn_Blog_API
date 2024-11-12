from django.shortcuts import render
from django.http import response, JsonResponse
from .models import *

def hello(request):
    blogs = Blog.objects.all()

    data ={
        "Blogs": list(blogs.values())
    }
    
    return JsonResponse(data)

def blog_detials(request,pk):
    blog = Blog.objects.get(pk=pk)

    data={
        "name": blog.name,
        "description": blog.description,
        "slug": blog.slug
    }

    return JsonResponse(data)

