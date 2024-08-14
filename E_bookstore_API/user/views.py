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

# Create a new user
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        # get the data from the request
        data = json.loads(request.body)
        # check if the data is valid
        if is_valid_form(data):
            # check if the email is valid
            if validate_email(data['email']):
                # check if the password is valid
                if validate_password(data['password']):
                    # create a new user
                    user = User.objects.create_user(data['email'], data['password'])
                    return JsonResponse({'message': 'User created successfully!'}, status=201)
                else:
                    return JsonResponse({'message': 'Password is invalid!'}, status=400)
            else:
                return JsonResponse({'message': 'Email is invalid!'}, status=400)
        else:
            return JsonResponse({'message': 'Data is invalid!'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed!'}, status=405)