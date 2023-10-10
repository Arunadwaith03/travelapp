from django.contrib.auth import login

from . import views
from django.urls import path


urlpatterns = [


    path('',views.demo, name='demo'),
    path('logout',views.logout,name='logout')

]
