from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def home(request):

    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response({
        'status':200 ,
        'resp': serializer.data
    })

@api_view(['POST'])
def save_student(request):
    data = request.data
    serializer= StudentSerializer(data=data)
    if not serializer.is_valid():
        return Response({
            'status':400 ,
            'resp': serializer.errors
        })
    serializer.save()
    return Response({
        'status':200 ,
        'resp': serializer.data
    })

"""
What is Difference between PUT and PATCH?
PUT: It is used to update all the fields of an existing resource.
Patch: It is used to update one or more fields of an existing resource.

If we simply use this line:
serializer= StudentSerializer(student,data=data), then we have to provide all the fields of the model.
In the request.data, if we don't provide all the fields of the model, then it will throw an error.

If we will use this line:
serializer= StudentSerializer(student,data=data, partial=True), then we don't have to provide all the fields of the model.
We will only provide the fields which we want to update. Rest of all the fields value will be taken from the database.  
"""

@api_view(['PUT'])
def update_student(request,id):
    try:
        data = request.data
        student = Student.objects.get(id=id)
        serializer= StudentSerializer(student,data=data,partial=True)
        if not serializer.is_valid():
            return Response({
                'status':400 ,
                'resp': serializer.errors
            })
        serializer.save()
        return Response({
            'status':200 ,
            'resp': serializer.data
        })
    except Exception as e:
        return Response({
            'status':400 ,
            'resp': str(e)
        })  
    

@api_view(['DELETE'])
def delete_student(request,id):  # sourcery skip: avoid-builtin-shadow
    try:
        
        student = Student.objects.get(id=id)
        student.delete()
        return Response({
            'status':200 ,
            'resp': "student deleted successfully"
        })
    except Exception as e:
        return Response({
            'status':400 ,
            'resp': str(e)
        })