from django.contrib import admin
from django.urls import path, include, re_path # 引用呼叫路由的方法

from jnc.settings import DEBUG # 用於判斷目前開發模式

from django.conf import settings
from django.conf.urls.static import static

# 引用前端路由使用
from django.views.generic import TemplateView

# 定義方法
from django.contrib.staticfiles.views import serve
from django.views.static import serve as static_serve # 注意這裏引入的與上面的不同
def return_static(request, path, insecure=True, **kwargs): 
    return serve(request, path, insecure, **kwargs)

# 【測試開發】: DEBUG = True(Deployment)
if( DEBUG ):
    urlpatterns = [
        re_path(r'^$', TemplateView.as_view(template_name="index.html")), # 配置前端路由

        path('admin/', admin.site.urls),
        path('', include('apps.devices_inspect.urls')), # 新增的app

        # 透過正則來去挑出路由
        re_path(r'^media/(?P<path>.*)$' , static_serve, { 'document_root' : settings.MEDIA_ROOT}),


        # 【解決Vue-Router History mode刷新頁面404的問題】https://blog.csdn.net/lucky__peng/article/details/124950853
        re_path(r'.*', TemplateView.as_view(template_name="index.html")), # 新增的(加在最後一段，這樣如果有找不到的內容都會被導引到index.html)
    ]


# 【正式上線】: DEBUG = False(Production)
else:
    urlpatterns = [
        re_path(r'^$', TemplateView.as_view(template_name="index.html")), # 配置前端路由

        path('admin/', admin.site.urls),
        path('api/', include('apps.devices_inspect.urls')), # 新增的app

        # 【解決Vue-Router History mode刷新頁面404的問題】https://blog.csdn.net/lucky__peng/article/details/124950853
        re_path(r'.*', TemplateView.as_view(template_name="index.html")), # 新增的(加在最後一段，這樣如果有找不到的內容都會被導引到index.html)
    ]