from django.contrib import admin
from django.urls import path,include
from .views import Data,index,register

urlpatterns = [

    path('', index, name = 'home'),
    path('register', register, name = 'register'),
    path('api/', Data.as_view() )
    

    
]
