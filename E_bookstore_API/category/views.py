from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from books.models import Book

class CategoryNames(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = []
        for category in categories:
            data.append({
                'name': category.name
            })
        return Response(data, status=status.HTTP_200_OK)
    
class CategoryList(APIView):
    def get(self, request, name):
        try:
            category = Category.objects.get(name=name)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        books = category.books.all()
        data = []
        for book in books:
            data.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'price': book.price,
                'cover': book.cover.url if book.cover else None
            })
        return Response(data, status=status.HTTP_200_OK)

# Create your views here.
