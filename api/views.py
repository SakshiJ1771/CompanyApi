# from django.shortcuts import render
# from rest_framework import viewsets
# from api.models import Company, Employee
# from api.serializers import CompanySerializer, EmployeeSerializer
# from rest_framework.decorators import action
# from rest_framework.response import Response

# # Create your views here.
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class=CompanySerializer

#     @action(detail=True,methods=['get'])
#     def employees(self,request,pk=None):
#         try:
#             company = Company.objects.get(pk=pk)
#             emps = Employee.objects.filter(company=company)
#             emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
#             return Response(emps_serializer.data)
#         except Exception as e:
#             print(e)
#             return Response({
#                 'message':'Error! Does not exist'
#             })    

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# 


# 

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer, EmployeeCreateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Error! Does not exist'
            }) 

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer  # Use the create serializer for POST requests

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializer
        return EmployeeSerializer  # Use the regular serializer for GET requests

class EmployeeUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer