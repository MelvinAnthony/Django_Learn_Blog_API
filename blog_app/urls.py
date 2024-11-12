from django.urls import path
from . import views
urlpatterns = [
    path('blog_list/',views.hello, name="Blog_List"),
    path('get_detials/<int:pk>/',views.blog_detials, name = "blog_detials"),
]
