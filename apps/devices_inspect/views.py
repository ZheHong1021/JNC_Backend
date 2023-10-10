from django.shortcuts import render

from devices_inspect.models import \
    JNCPositionModel, JNCDeviceModel, JNCInspectModel, JNCInspectHistoryModel

from devices_inspect.serializers import \
    JNCPositionSerializer, JNCPositionInspectSerializer, JNCInspectSerializer
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

# JNC 設備
class JNCPositionList(generics.ListCreateAPIView):
    queryset = JNCPositionModel.objects.all()
    serializer_class = JNCPositionSerializer

class JNCPositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCPositionModel.objects.all()
    serializer_class = JNCPositionInspectSerializer

# JNC 檢測紀錄
class JNCInspectList(generics.ListCreateAPIView):
    queryset = JNCInspectModel.objects.all()
    serializer_class = JNCInspectSerializer


class JNCInspectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCInspectModel.objects.all()
    serializer_class = JNCInspectSerializer