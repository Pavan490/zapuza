from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from.models import*
from.serializers import*
from rest_framework import status
from rest_framework import viewsets
class Studentview(viewsets.ViewSet):
    def list(self,request):
        queryset=Employee.objects.all()
        serializer=EmployeeSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
          queryset=Employee.objects.get(id=id)
          serializer=EmployeeSerializer(queryset)
          return Response(serializer.data)
    def update(self,request,pk):
        id=pk
        queryset=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response({'msg':'Data is Updated'})
        return Response(serializer.errrs,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        id=pk
        queryset=Employee.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'Data is Deleted'}) 
    def create(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'msg':'Data is Created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
           
