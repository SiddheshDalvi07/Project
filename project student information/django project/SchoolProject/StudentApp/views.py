from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
def studentApi(request,id=0):
    if request.method=='GET':
        student = Student.objects.all()
        student_serializer=StudentSerializer(student,many=True)
        return Response(student_serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response("Added Successfully",status=status.HTTP_201_CREATED)
        return Response("Failed to Add",student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(id=id)
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response("Updated Successfully",status=status.HTTP_200_OK)
        return Response("Failed to Update",student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student=Student.objects.get(id=id)
        student.delete()
        return Response("Deleted Successfully",status=status.HTTP_204_NO_CONTENT)