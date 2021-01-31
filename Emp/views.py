from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from . models import employees
from . serializers import employeesSerializer
from rest_framework import generics


# Create your views here.

global data;
data = ["test"]

class EmpView(APIView):
    def get(self, request, format=None):
        message = {
            'Response' : 200,
            'Message' : "Welcome to Django REST API View"
        }
        return Response(message)
 
    def post(self, request, format=None):
        test_data = request.data
        name = test_data.get("name", None)
        data.append(name)
        message = {
            'Response' : 200,
            'Message' : "Welcome to Django REST API View",
            'data' : data
        }
        
        return Response(message)

class employeeList(APIView):
    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many = True)
        return Response(serializer.data)

    def post(self, request):
        pass


class employeeAdd(generics.CreateAPIView):
    serializer_class = employeesSerializer

    def create(self, request, *args, **kwargs):

        emp_id = request.data.get('Employee Id')
        firstname = request.data.get('First Name')
        lastname = request.data.get('Last Name')
        phone = request.data.get('Phone Number')
        email = request.data.get('Email Id')
        return super().create(request, *args, **kwargs)

