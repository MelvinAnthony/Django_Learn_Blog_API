from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


from rest_framework import mixins, generics

# -------------- Funtion based Views
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

# --------------- class Based views
class CategoryListViews(APIView):
    def get(self,request):
        all_category = Category.objects.all()
        serializer = CategorySerializer(all_category, many = True, context = {'request' : request})
        return Response(serializer.data)
    
class CategoryDetialViews(APIView):
    def get(self,request, pk):
        single_category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(single_category, context = {'request' : request})
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
    


# --------------------- generic view --------------------------------

class BlogListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        # Handle GET requests
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle POST requests
        return self.create(request, *args, **kwargs)

class BlogDetialGenericView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin ,generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        # Handle Get Specific requests
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        # Handle PUT requests
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        # Handle delete requests
        return self.destroy(request, *args, **kwargs)
    



# -------------- Concrete View Classes

class BlogCreateCon(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer


class BlogListCon(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer


class BlogReteriveCon(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer


class BlogDestoryCon(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer


class BlogUpdateCon(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer