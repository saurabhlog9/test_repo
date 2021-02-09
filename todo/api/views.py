from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


@api_view(['GET'])
def apioverview(request):
    api_url={
        'list':'/List of task/',
    }
    return Response(api_url)

@api_view(['GET'])
def tasklist(request):
    tasks=Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    tasks=Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks,many=False)

    return Response(serializer.data)

@api_view(['GET'])
def get_form(request):
    serializer = TaskSerializer()
    return Response(serializer)