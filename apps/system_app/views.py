from django.shortcuts import render
from rest_framework import viewsets
from system_app.models import Author, Book
from system_app.serializer import AuthorSerializer, BookSerializer

# Create your views here.
def error_500(request):
    return render(request, '500_Error.html')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer