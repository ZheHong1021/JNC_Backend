from django.shortcuts import render
from devices_inspect.models import JNCDeviceModel, JNCInspectModel
from devices_inspect.serializers import JNCDeviceSerializer, JNCInspectSerializer
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
class JNCDeviceList(generics.ListCreateAPIView):
    queryset = JNCDeviceModel.objects.all()
    serializer_class = JNCDeviceSerializer
    # permission_classes = [IsAuthenticated]


class JNCDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCDeviceModel.objects.all()
    serializer_class = JNCDeviceSerializer
    # permission_classes = [IsAuthenticated]

# JNC 檢測紀錄
class JNCInspectList(generics.ListCreateAPIView):
    queryset = JNCInspectModel.objects.all()
    serializer_class = JNCInspectSerializer
    # permission_classes = [IsAuthenticated]


class JNCInspectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCInspectModel.objects.all()
    serializer_class = JNCInspectSerializer
    # permission_classes = [IsAuthenticated]