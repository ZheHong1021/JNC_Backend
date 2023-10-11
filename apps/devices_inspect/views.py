from django.shortcuts import render

from devices_inspect.models import \
    JNCPositionModel, JNCDeviceModel, JNCInspectModel, JNCInspectHistoryModel

from devices_inspect.serializers import \
    JNCPositionSerializer, JNCPositionInspectSerializer, \
    JNCDeviceSerializer, JNCInspectSerializer, JNCInspectHistorySerializer

from django.http import HttpResponse

#region 【DRF】
from rest_framework import generics
#endregion

# # Create your views here.
# def renderDevicesPage(request):
#     # QuerySet -> 從資料庫中搜尋的結果
#     devices = JNCDeviceModel.objects.all()
    
#     # return HttpResponse({tokens})
#     return render(request, 'home.html', {
#         'devices': devices,
#     })

# 【監測設備】
class JNCDeviceList(generics.ListCreateAPIView):
    queryset = JNCDeviceModel.objects.all()
    serializer_class = JNCDeviceSerializer

class JNCDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCDeviceModel.objects.all()
    serializer_class = JNCDeviceSerializer

    
# 【監測場域】
class JNCPositionList(generics.ListCreateAPIView):
    queryset = JNCPositionModel.objects.all()
    serializer_class = JNCPositionSerializer

class JNCPositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCPositionModel.objects.all()
    serializer_class = JNCPositionInspectSerializer


# 【監測數據 - 即時】
class JNCInspectList(generics.ListCreateAPIView):
    queryset = JNCInspectModel.objects.all()
    serializer_class = JNCInspectSerializer

class JNCInspectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCInspectModel.objects.all()
    serializer_class = JNCInspectSerializer


# 【監測數據 - 歷史】
class JNCInspectHistoryList(generics.ListCreateAPIView):
    queryset = JNCInspectHistoryModel.objects.all()
    serializer_class = JNCInspectHistorySerializer

class JNCInspectHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCInspectHistoryModel.objects.all()
    serializer_class = JNCInspectHistorySerializer