from django.shortcuts import render

# Create your views here.
# we're building a REST API, so we don't need to render any templates
# we need to return JSON responses
# we need to use Django's JsonResponse class to return JSON responses
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from .utils import is_valid_form, validate_email, validate_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create a new user
# POST /api
# we would like to create a class based view

class loginAPI(APIView):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not validate_email(email):
            return Response({'error': 'Please enter a valid email address'}, status=status.HTTP_400_BAD_REQUEST)
        if not validate_password(password):
            return Response({'error': 'Password must be at least 8 characters long'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=email, password=password).first()
        if not user:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

class registerAPI(APIView):
    def post(self, request):
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        if not first_name:
            return Response({'error': 'First name is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not last_name:
            return Response({'error': 'Last name is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not validate_email(email):
            return Response({'error': 'Please enter a valid email address'}, status=status.HTTP_400_BAD_REQUEST)
        if not validate_password(password):
            return Response({'error': 'Password must be at least 8 characters long'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=email).first()
        if user:
            return Response({'error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)