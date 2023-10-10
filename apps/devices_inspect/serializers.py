from rest_framework import serializers
from devices_inspect.models import \
    JNCPositionModel, JNCDeviceModel, JNCInspectModel, JNCInspectHistoryModel

# 【監測數據】
class JNCInspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = JNCInspectModel
        ordering = ['id']
        fields = '__all__'
    


# 【監測場域】
class JNCPositionSerializer(serializers.ModelSerializer):
    # 檢測項目數量
    inspect_num = serializers.SerializerMethodField() 
    class Meta:
        model = JNCPositionModel
        ordering = ['id']
        fields = '__all__'
        
    def get_inspect_num(self, instance):
        return instance.inspects.count()
    
# 【監測場域】(含檢測數據(即時))
class JNCPositionInspectSerializer(serializers.ModelSerializer):
    # 檢測項目數量
    inspects = serializers.SerializerMethodField() 
    class Meta:
        model = JNCPositionModel
        ordering = ['id']
        fields = '__all__'
        
    def get_inspects(self, instance):
        # 直接做排序後再回傳 Serializer
        inspects = instance.inspects.order_by('id')

        # 記得要有.data
        return JNCInspectSerializer(inspects, many=True).data
    





    