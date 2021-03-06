from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers

class HelloApiView(APIView):

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    an_apiview = [
      'Uses HTTp methods as functions (get, post, ptach, put, delete)',
      'Is similar to a traditional Django View',
      'Gives you the most control over you application logic',
      'Is mapped manually to URLs'
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})
  
  def post(self, request): 
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'

      return Response({'message': message})

    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

class HelloViewSet(viewsets.ViewSet):
  serializer_class = serializers.HelloSerializer

  def list(self, request):
    a_viewset = [
      'Uses actions (list, create, retrive, update, partial_update)',
      'Automatically maps to URLs using Routers',
      'Provides more functionality with less code'
    ]

    return Response({'message': 'Hello!', 'a_viewset': a_viewset})
  
  def create(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'

      return Response({'message': message})

    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )
  
  def retrieve(self, request, pk=None):
    return Response({'http_method': 'GET'})

  def update(self, request, pk=None):
    return Response({'http_method': 'PUT'})

  def partial_update(self, request, pk=None):
    return Response({'http_method': 'PATCH'})

  def destroy(self, request, pk=None):
    return Response({'http_method': 'DELETE'})
