from django.shortcuts import render

from devices_inspect.models import \
    JNCPositionModel, JNCDeviceModel, JNCInspectModel, JNCInspectHistoryModel

from devices_inspect.serializers import \
    JNCPositionSerializer, JNCPositionInspectSerializer, \
    JNCDeviceSerializer, JNCInspectSerializer, JNCInspectHistorySerializer

from django.http import HttpResponse
from datetime import datetime, date
import datetime as dt
import json

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
    def get_queryset(self): # 調用 get_queryset函式        
        # 【1】request.GET返回一個QueryDict對象。
        # 【2】get()方法可以用來獲取指定鍵的值。
        # 【3】如果該鍵不存在，則返回None
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        inspect_id = self.request.GET.get('inspect_id', None)
        qs = super().get_queryset() # 得到 QuerySet
        filters = {} # 透過這樣方式去做篩選
        
        if inspect_id:
            filters['inspect_id__id__in'] = json.loads(inspect_id)
        else: # 多數篩選
            filters['inspect_id__id__in'] = [2, 3, 4, 5]

        
        if start_date and end_date:

            # filters['created_at__range'] = (start_date, end_date)
            filters['created_at__range'] = (
                datetime.combine( datetime.strptime(start_date, '%Y-%m-%d'), dt.time.min ), 
                datetime.combine( datetime.strptime(end_date, '%Y-%m-%d'), dt.time.max )
            )
        else:
            filters['created_at__range'] = ('2023-10-11 00:00:00', '2023-10-11 10:59:59')
            # filters['created_at__range'] = ('2023-10-10 00:00:00', '2023-10-11 23:59:59')
            # filters['created_at__range'] = (
            #     datetime.combine( date.today(), dt.time.min ), 
            #     datetime.combine( date.today(), dt.time.max )
            # )
     
        if filters:
            qs = qs.filter(**filters)

        return qs # 如果找不到Request則回傳全部

class JNCInspectHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JNCInspectHistoryModel.objects.all()
    serializer_class = JNCInspectHistorySerializer
    