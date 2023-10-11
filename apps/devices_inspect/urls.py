from django.urls import path
from . import views

urlpatterns = [
    # path("", views.renderDevicesPage)

    # 【監測場域】
    path('positions', views.JNCPositionList.as_view()),
    path('position/<int:pk>', views.JNCPositionDetail.as_view()),

    # 【監測設備】
    path('devices', views.JNCDeviceList.as_view()),
    path('device/<int:pk>', views.JNCDeviceDetail.as_view()),

    # 【監測數據 - 即時】
    path('inspects', views.JNCInspectList.as_view()),
    path('inspect/<int:pk>', views.JNCInspectDetail.as_view()),

    # 【監測數據 - 歷史】
    path('history-inspects', views.JNCInspectHistoryList.as_view()),
    path('history-inspect/<int:pk>', views.JNCInspectHistoryDetail.as_view()),
]