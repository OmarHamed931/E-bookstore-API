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
    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if user:
            return Response({'error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username).first()
        if user:
            return Response({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username , email=email, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)