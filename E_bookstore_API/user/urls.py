from django.urls import path 
from .views import registerAPI, loginAPI
urlpatterns = [
    path('register/', registerAPI.as_view(), name='register'),
    path('login/', loginAPI.as_view(), name='login'),
    
]