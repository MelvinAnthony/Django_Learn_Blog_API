from django.urls import path
from . import views
urlpatterns = [

    
                        #manual GET,POST,PUT,DELETE method path
    # path('blog_list/',views.blog_list, name="Blog_List"),
    # path('get_detials/<int:pk>/',views.blog_detials, name = "blog_detials"),


                # Create class based urls
    path('class_blog_list/', views.BlogListView.as_view(), name= "all_blog_list"),
    path('class_blog_detial/<int:pk>/', views.BlogDetialsView.as_view(),name = "detial_blog")

            
]
