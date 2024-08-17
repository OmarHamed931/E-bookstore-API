from operator import is_
from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'created_at', 'updated_at']
# Compare this snippet from E_bookstore_API/user/urls.py:

