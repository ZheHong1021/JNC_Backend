"""
URL configuration for jnc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path # 引用呼叫路由的方法

from jnc.settings import DEBUG # 用於判斷目前開發模式


# 【測試開發】: DEBUG = True(Deployment)
if( DEBUG ):
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('apps.devices_inspect.urls')), # 新增的app
        path('api/', include('apps.system_app.urls')), # 新增的app
    ]


# 【正式上線】: DEBUG = False(Production)
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('apps.devices_inspect.urls')), # 新增的app
        path('api/', include('apps.system_app.urls')), # 新增的app
    ]