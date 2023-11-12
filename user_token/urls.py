from django.urls import path, include
from rest_framework import routers

from user_token.views import UserViewSet, CustomAuthToken
from rest_framework.authtoken import views # 權限

# 自動決定URL Conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token)
    path('api-token-auth/', CustomAuthToken.as_view())
]