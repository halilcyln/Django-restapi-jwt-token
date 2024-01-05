# myapp/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookListView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
