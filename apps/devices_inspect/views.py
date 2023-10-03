from django.shortcuts import render
from devices_inspect.models import JNCDeviceModel
from django.http import HttpResponse

# # Create your views here.
# def renderDevicesPage(request):
#     # QuerySet -> 從資料庫中搜尋的結果
#     devices = JNCDeviceModel.objects.all()
    
#     # return HttpResponse({tokens})
#     return render(request, 'home.html', {
#         'devices': devices,
#     })