from django.db import models


class AccessTokenModel(models.Model):
    name = models.CharField('Token使用的場', max_length=255)
    token = models.TextField('Token')
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)
    class Meta:
        db_table = 'access_token'
        verbose_name = "推播權杖儲存" 
        verbose_name_plural = "推播權杖儲存管理"
        ordering = ('created_at',)


class JNCDeviceModel(models.Model):
    DeviceName = models.CharField('設備名稱', max_length=255)
    JNCDevice = models.CharField('設備項目(I6_Web、Feeder、Weather_Station、CloudBox、VirtualDevice)', max_length=255)
    GPSx = models.DecimalField("經度(Longitude)", max_digits=9, decimal_places=6)
    GPSy = models.DecimalField("緯度(Latitude)", max_digits=8, decimal_places=6)
    Connect = models.BooleanField("有無連線")
    USB = models.IntegerField("(-1、0、2、3)")
    SIM = models.IntegerField("(-1、0、4、10)")
    device_url = models.TextField("設備API url")
    inspect_url = models.TextField("檢測API url")
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    # 這邊資料表中欄位命名為 postion_id，不用特別再寫_id，Django會自動補上
    # position = models.ForeignKey(PositionModel, on_delete=models.CASCADE)
    # 加上 db_column這樣子Django就不會自動加入後綴_id了
    token_id = models.ForeignKey(
        AccessTokenModel, 
        related_name="devices", # 反向關聯(在AccessTokenModel時可以呼叫Devices列表)
        db_column="token_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True
    )
    class Meta:
        db_table = 'jnc_device'
        verbose_name = "檢測設備列表" 
        verbose_name_plural = "檢測設備管理"
        ordering = ('created_at',)


class JNCInspectModel(models.Model):
    ChType = models.CharField('Channel類型 (AI、DO、DI、VO)', max_length=50)
    TagName = models.CharField('', max_length=255)
    Unit = models.CharField('單位', max_length=50, default=None)
    IsEnable = models.BooleanField("有無啟動")
    Value = models.FloatField("檢測數值結果")
    AlarmState = models.CharField('警告狀態(Discon、Normal、LO)', max_length=50)
    IsRead = models.BooleanField("")
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    # 這邊資料表中欄位命名為 postion_id，不用特別再寫_id，Django會自動補上
    # position = models.ForeignKey(PositionModel, on_delete=models.CASCADE)
    # 加上 db_column這樣子Django就不會自動加入後綴_id了
    device_id = models.ForeignKey(
        JNCDeviceModel, 
        related_name="inspects", # 反向關聯(在AccessTokenModel時可以呼叫Devices列表)
        db_column="device_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True
    )
    class Meta:
        db_table = 'jnc_inspect'
        verbose_name = "檢測數據列表" 
        verbose_name_plural = "檢測數據管理"
        ordering = ('created_at',)


class JNCInspectHistoryModel(models.Model):
    Unit = models.CharField('單位', max_length=50, default=None)
    IsEnable = models.BooleanField("有無啟動")
    Value = models.FloatField("檢測數值結果")
    AlarmState = models.CharField('警告狀態(Discon、Normal、LO)', max_length=50)
    IsRead = models.BooleanField("")
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    # 這邊資料表中欄位命名為 postion_id，不用特別再寫_id，Django會自動補上
    # position = models.ForeignKey(PositionModel, on_delete=models.CASCADE)
    # 加上 db_column這樣子Django就不會自動加入後綴_id了
    inspect_id = models.ForeignKey(
        JNCInspectModel, 
        related_name="historys", # 反向關聯(在AccessTokenModel時可以呼叫Devices列表)
        db_column="inspect_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True
    )
    class Meta:
        db_table = 'jnc_inspect_history'
        verbose_name = "歷史檢測數據列表" 
        verbose_name_plural = "歷史檢測數據管理"
        ordering = ('created_at',)
