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

def post()