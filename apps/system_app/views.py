from django.shortcuts import render
from rest_framework import viewsets
from system_app.models import Author, Book
from system_app.serializer import AuthorSerializer, BookSerializer

from drf_spectacular .utils import extend_schema # 引用
# Create your views here.
def error_500(request):
    return render(request, '500_Error.html')

@extend_schema(responses=AuthorSerializer)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@extend_schema(responses=BookSerializer)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer