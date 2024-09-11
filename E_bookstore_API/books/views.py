from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book



class BookList(APIView):
    #get all books and sends them to the client
    def get(self, request):
        books = Book.objects.all()
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

class BookDetail(APIView):
    #get a single book and sends it to the client
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        data = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'description': book.description,
            'price': book.price,
            'published_at': book.published_at,
            'cover': book.cover.url if book.cover else None
        }
        return Response(data, status=status.HTTP_200_OK)
class FeaturedBooks(APIView):
    def get(self, request):
        # get the newest 5 books
        books = Book.objects.order_by('-id')[:5]
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
