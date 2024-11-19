from django.urls import path
from . import views
urlpatterns = [

    
                        #manual GET,POST,PUT,DELETE method path
    # path('blog_list/',views.blog_list, name="Blog_List"),
    # path('get_detials/<int:pk>/',views.blog_detials, name = "blog_detials"),


                # Create class based urls
    path('class_blog_list/', views.BlogListView.as_view(), name= "all-blog-list"),
    path('class_blog_detial/<int:pk>/', views.BlogDetialsView.as_view(),name = "detial-blog"),

                    # category URLs
    path('category_list/',views.CategoryListViews.as_view(), name='category-list'),
    path('category_detial/<int:pk>/',views.CategoryDetialViews.as_view(), name='category-detial'),


                # Generic Views
    path('blog_list_generic_view/', views.BlogListGenericView.as_view(), name = "blog_list_generic_view"),
    path('blog_speciic_generic_view/<int:pk>/', views.BlogDetialGenericView.as_view(), name = "blog_specific_generic_view"),



            
]
