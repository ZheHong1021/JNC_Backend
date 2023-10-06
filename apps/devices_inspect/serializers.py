from rest_framework import serializers
from devices_inspect.models import JNCDeviceModel, JNCInspectModel # 引用Model


class JNCDeviceSerializer(serializers.ModelSerializer):
    # 檢測項目數量
    inspect_num = serializers.SerializerMethodField() 
    class Meta:
        model = JNCDeviceModel
        ordering = ['id']
        fields = '__all__'
        
    def get_inspect_num(self, instance):
        return instance.inspects.count()

class JNCInspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = JNCInspectModel
        ordering = ['id']
        fields = '__all__'
    
    