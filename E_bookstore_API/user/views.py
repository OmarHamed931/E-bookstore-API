from django.shortcuts import render

# Create your views here.
# we're building a REST API, so we don't need to render any templates
# we need to return JSON responses
# we need to use Django's JsonResponse class to return JSON responses
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

# Create a new user
# POST /api
# we would like to create a class based view

class loginAPI(APIView):
    def post(self, request):
        #it's a multipart form data
        data = request.data
        username = data.get('username')
        password = data.get('password')
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token' : token.key }, status=status.HTTP_200_OK) 

class registerAPI(APIView):
    # implement the post method using serializers
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # i want to make sure that the user is created
            # i want to return a token to the user
            user= User.objects.get(username=user.username)


            if not user:
                return Response({'error': 'User not created'}, status=status.HTTP_400_BAD_REQUEST)
            token, created = Token.objects.get_or_create(user=user)
            if not token:
                return Response({'error': 'Token not created'}, status=status.HTTP_400_BAD_REQUEST)

            # Debug statements
            print(f"User: {user.username}")
            print(f"Token: {token.key}")
            print(f"Token Created: {created}")

            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
            

            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
