# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BookListView

router = DefaultRouter()
router.register(r'text', BookListView, basename='text')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
