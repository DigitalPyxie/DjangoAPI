import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

#creating a logger
logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def task_list_create(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            task = serializer.save()

            #POST logger*
            logger.info(f"Task created: {task.title}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        #ERROR logger *
        logger.error(serializer.errors)

        #validation failure
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):

    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    #to view single task
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    #to edit/update the tast
    if request.method == 'PUT':
        serializer = TaskSerializer(task,data=request.data)

        if serializer.is_valid():
            task = serializer.save()

            #PUT logger*
            logger.info(f"Task updated: {task.title}")

            return Response(serializer.data)

        #ERROR logger*
        logger.error(serializer.errors)

        #Validation failure    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #to delete
    if request.method == 'DELETE':

        #DELETE logger**
        logger.info(f"Task deleted: {task.title}")

        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)         

