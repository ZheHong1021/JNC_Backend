from django.urls import path
from . import views

urlpatterns = [
    # path("", views.renderDevicesPage)

    # 【監測設備】
    path('devices', views.JNCDeviceList.as_view()),
    path('device/:id', views.JNCDeviceDetail.as_view()),


    # 【監測數據】
    path('inspects', views.JNCInspectList.as_view()),
    path('inspect/:id', views.JNCInspectDetail.as_view()),
]