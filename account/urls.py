from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("login/",obtain_auth_token, name="login"),
    path("log_out/",views.log_out, name="log_out")
    

]