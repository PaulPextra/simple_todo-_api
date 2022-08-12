from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from . models import Todo
from . serializers import TodoSerializer, TodoListSerializer

@swagger_auto_schema(methods=['POST'], request_body=TodoSerializer())
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo_obj = Todo.objects.all()
        serializer_class = TodoListSerializer(todo_obj, many=True)
        
        context = {
            'message': 'success',
            'data': serializer_class.data
        }
        
        return Response(context, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer_class = TodoSerializer(data=request.data)
        
        if serializer_class.is_valid():
            todo_obj = Todo.objects.create(**serializer_class.validated_data)
            serializer_class = TodoSerializer(todo_obj)
            
            context = {
                'message': 'Success',
                'data': serializer_class.data
            }
            
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=TodoSerializer())
@api_view(['GET', 'PUT', 'DELETE'])     
def todo_detail(request, todo_id):
    try:
        todo_obj = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        context = {
            'status': False,
            'message': 'Does not exist'
        }
        
        return Response(context, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer_class = TodoSerializer(todo_obj)
        
        context = {
            'status': True,
            'message': 'Success',
            'data': serializer_class.data
        }
        
        return Response(context, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer_class = TodoSerializer(todo_obj, data=request.data, partial=True)
        
        if serializer_class.is_valid():
            serializer_class.save()
            
            context = {
                'status': True,
                'message': 'Success',
                'data': serializer_class.data
            }
            
            return Response(context, status=status.HTTP_202_ACCEPTED)
        else:
            context = {
                'status': False,
                'message': 'Failed',
                'error': serializer_class.errors
            }
            
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo_obj.delete()
        
        context = {
            'status': True,
            'message': 'Success'
        }
        
        return Response(context, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def mark_complete(request, todo_id):
    try:
        todo_obj = Todo.objects.get(id = todo_id)
    except Todo.DoesNotExist:
        
        data = {
            'status'  : False,
            'message' : 'Does not exist'
        }

        return Response(data, status = status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        
        if todo_obj.completed == False:
            
            todo_obj.completed = True
            
            todo_obj.save()
                  
            context = {
                'status'  : True,
                'message' : 'Successful'
            }

            return Response(context, status = status.HTTP_200_OK)
        
        else:
                  
            context = {
                'status'  : False,
                'message' : 'Already marked complete'
            }

            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    