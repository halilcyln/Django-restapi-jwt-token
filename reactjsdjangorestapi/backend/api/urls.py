
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('text/', BookListView.as_view(), name='note-list-create'),
]
