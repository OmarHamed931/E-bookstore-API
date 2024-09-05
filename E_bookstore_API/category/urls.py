from django.urls import path
from .views import CategoryList , CategoryNames

urlpatterns = [
    path('', CategoryNames.as_view(), name='category-names'),
    path('<str:name>/', CategoryList.as_view(), name='category-list'),
]
