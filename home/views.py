from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import Registration
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import  status
from . serializers import Serializer

# Create your views here.
def index(request):
    context={
        'variable':'Rachana'
    }
    messages.success(request, 'test message')
    return render(request,'index.html',context)
    #return HttpResponse("this is homepage")


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        register = Registration(name = name, email = email, password = password)
        register.save()
        messages.success(request, 'Registered Successfully')
    return render(request,'register.html')


class Data(APIView):
    def get(self,request):
        data=Registration.objects.all()
        serializer=Serializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass