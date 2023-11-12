from django.urls import path, include
from rest_framework.routers import DefaultRouter
from system_app import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
]