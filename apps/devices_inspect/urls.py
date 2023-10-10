from django.urls import path
from . import views

urlpatterns = [
    # path("", views.renderDevicesPage)

    # 【監測場域】
    path('positions', views.JNCPositionList.as_view()),
    path('position/<int:pk>', views.JNCPositionDetail.as_view()),


    # 【監測數據】
    path('inspects', views.JNCInspectList.as_view()),
    path('inspect/<int:pk>', views.JNCInspectDetail.as_view()),
]