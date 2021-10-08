from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users
from .forms import UsersForm
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        users = Users.objects.all()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = Users.objects.get(username=serializer.validated_data['username'])
            form = UsersForm(serializer.validated_data, instance=user)
            form.save()
            return Response('Updated user data', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User = Users.objects.get(username=serializer.validated_data['username'])
            User.delete()
            return Response("Successfully deleted user", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)