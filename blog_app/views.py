from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


from rest_framework import mixins, generics
from rest_framework import viewsets, serializers

from django.shortcuts import *


from rest_framework.permissions import *


from .permissions import *


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


class BlogReteriveDestoryApiView(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer

class BlogListCreateApiView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer

class BlogRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer


# ---------------- Views Set
# class BlogViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Blog.objects.filter(is_public = True)
#         serializer = BlogSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = Blog.objects.filter(is_public = True)
#         blog_list = get_object_or_404(queryset, pk=pk)
#         serializer = BlogSerializer(blog_list)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = BlogSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk=None):
#         blog = get_object_or_404(Blog, pk=pk)
#         serializer = BlogSerializer(blog,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self,request, pk=None):
#         blog = get_object_or_404(Blog, pk=pk)
#         blog.delete()
#         return Response({"message": "Your Blog was deleted"}, status=status.HTTP_204_NO_CONTENT)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializer

#  ------------------------ Create a blog view using generics

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True, context = {'request': request})

        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({'message':'blog not found'}, status=status.HTTP_204_NO_CONTENT)


    
    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author = self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class BlogDetialCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializer
    liikup_field = 'id' # or slug
    permission_classes = [IsOwnerorReadonly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({'message':'blog not found'}, status=status.HTTP_204_NO_CONTENT)
        
#                category based
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # it need login for view the class
    #permission_classes = [IsAuthenticated]   
    
    # it need login using admin user to view
    #permission_classes = [IsAdminUser]   
    
    # using login to edit the detial or hav the permission to view the data
    #Custom Permission: if user has admin he can able to perform CURD operation and not as admin means only read only option avilabile
    permission_classes = [IsAdminUserorReadOnly]   

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True, context = {'request': request})

        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
class CategoryDetialCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerorReadonly]

   
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({'message':'blog not found'}, status=status.HTTP_204_NO_CONTENT)
        

#       Blog Comment List View
class BlogCommentListCreateView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        return BlogComment.objects.filter(blog_id=blog_id)
    
    def perform_create(self, serializer):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog, id = blog_id)
        if BlogComment.objects.filter(blog=blog, author = self.request.user).exists():
            raise serializers.ValidationError({"Message": "You have already done your command on Blog!!"})
        serializer.save(author=self.request.user, blog=blog)


class BlogCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsOwnerorReadonly]
    
    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(BlogComment, id = comment_id)
        
        blog_id = self.kwargs.get("blog_id")
        if comment.blog.id != blog_id:
            raise serializers.ValidationError({"Message": "This comment is not related to the requested blog"}, status=status.HTTP_401_UNAUTHORIZED)
        return comment
    
    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)