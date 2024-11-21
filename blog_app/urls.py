from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs',views.BlogViewSet, basename='blog')

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
    #path('blog_speciic_generic_view/<int:pk>/', views.BlogDetialGenericView.as_view(), name = "blog_specific_generic_view"),
    path('blog_speciic_generic_view/<str:slug>/', views.BlogDetialGenericView.as_view(), name = "blog_specific_generic_view"),


                # Concrete View
    path('blog_create_createapiview/',views.BlogCreateCon.as_view(), name='blog_create_createapiview'),
    path('blog_list_createapiview/',views.BlogListCon.as_view(), name='blog_list_createapiview'),
    path('blog_reterive_createapiview/<int:pk>/',views.BlogReteriveCon.as_view(), name='blog_reterive_createapiview'),
    path('blog_destory_createapiview/<int:pk>/',views.BlogDestoryCon.as_view(), name='blog_destory_createapiview'),
    path('blog_update_createapiview/<int:pk>/',views.BlogUpdateCon.as_view(), name='blog_update_createapiview'),
    
    
    
    path('blog_reterive_destory_createapiview/<int:pk>/',views.BlogReteriveDestoryApiView.as_view(), name='blog_reterive_destory_createapiview'),
    path('blog_list_create_createapiview/',views.BlogListCreateApiView.as_view(), name='blog_list_create_createapiview'),
    path('blog_create_update_delete_createapiview/<int:pk>/',views.BlogRUDApiView.as_view(), name='blog_create_update_delete_createapiview'),


                    #ViewSet
    path('',include(router.urls)),

    #  ------------------------ Create a blog view using generics
    path('blog_list/',views.BlogListCreateView.as_view(), name = 'blog_list'),
    path('blog_detial/<int:pk>/',views.BlogDetialCreateView.as_view(), name = 'blog_detial'),
    path('blog_category_list/',views.CategoryListCreateView.as_view(), name = 'blog_category_list'),
    path('blog_category_detial/<int:pk>/',views.CategoryDetialCreateView.as_view(), name = 'blog_category_detial'),


    # ------------------------ Comment blog 
    path('blog_commant_list/<int:blog_id>/',views.BlogCommentListCreateView.as_view(), name = 'blog_commant_list'),
    path('blog_commant_detial/blog/<int:blog_id>/comment/<int:comment_id>/',views.BlogCommentDetailView.as_view(), name = 'blog_commant_detial'),   
    
            
]
