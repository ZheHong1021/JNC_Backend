from django.db import models
from devices_inspect.models import JNCInspectModel
from datetime import datetime

# 推播權杖
class NotifyTokenModel(models.Model):
    name = models.CharField('Token使用的場', max_length=255)
    token = models.TextField('Token')
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)
    class Meta:
        db_table = 'notify_token'
        verbose_name = "推播權杖儲存" 
        verbose_name_plural = "推播權杖儲存管理"
        ordering = ('created_at',)


# 推播設備群組
class NotifyDeviceModel(models.Model):
    name = models.CharField('群組名稱', max_length=255)
    ClientID = models.CharField('Notify設備ID', max_length=255)
    CallBackURL = models.TextField('回調回來的URL')
    ClientSecret = models.TextField('Secret', max_length=255)
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    token_id  = models.ForeignKey(
        NotifyTokenModel, 
        related_name="devices", # 反向關聯(在AccessTokenModel時可以呼叫Devices列表)
        db_column="token_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True,
        default=None
    )
    class Meta:
        db_table = 'notify_device'
        verbose_name = "推播設備群組" 
        verbose_name_plural = "推播設備群組管理"
        ordering = ('created_at',)

# 推播事件
class NotifyEventModel(models.Model):
    name = models.CharField('事件名稱', max_length=255)
    message = models.TextField('事件訊息通知')
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    device_id  = models.ForeignKey(
        NotifyDeviceModel, 
        related_name="events", # 反向關聯(在AccessTokenModel時可以呼叫Devices列表)
        db_column="device_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True,
        default=None
    )
    class Meta:
        db_table = 'notify_event'
        verbose_name = "推播事件" 
        verbose_name_plural = "推播事件管理"
        ordering = ('created_at',)


# 條件列表(= 、 > 、 <)
class Statement(models.Model):
    id = models.CharField('lte、gte、lt、gt、equal、like', max_length=50, primary_key=True)
    name = models.CharField('大於等於、小於等於、大於、等於...', max_length=255)
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    class Meta:
        db_table = 'statement'
        verbose_name = "條件列表" 
        verbose_name_plural = "條件列表管理"
        ordering = ('created_at',)


# 推播事件條件
class NotifyStatementModel(models.Model):
    name = models.CharField('事件名稱', max_length=255)
    statement = models.TextField('條件定義(依照『;』分號區隔多個條件式-AND)')
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    event_id  = models.ForeignKey(
        NotifyEventModel, 
        related_name="statements", # 反向關聯(events列表)
        db_column="event_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True,
        default=None
    )
    statement_id  = models.ForeignKey(
        Statement, 
        related_name="notify_statement", # 反向關聯(events列表)
        db_column="statement_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True,
        default=None
    )

    jnc_inspect_id  = models.OneToOneField(
        JNCInspectModel, 
        related_name="notify_statement", # 反向關聯(events列表)
        db_column="jnc_inspect_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True,
        default=None
    )

    class Meta:
        db_table = 'notify_statement'
        verbose_name = "推播事件條件" 
        verbose_name_plural = "推播事件條件管理"
        ordering = ('created_at',)



# 推播警告紀錄
class AlertLogModel(models.Model):
    id = models.CharField('<日期字串縮減>_<事件ID>', max_length=50, primary_key=True)
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)

    event_id  = models.ForeignKey(
        NotifyEventModel, 
        related_name="alerts", # 反向關聯(events列表)
        db_column="event_id", # 欄位名稱(可以捕捉到上一層AccessTokenModel的資料)
        on_delete=models.CASCADE, 
        null=True,
        default=None
    )

    class Meta:
        db_table = 'alert_log'
        verbose_name = "推播警告紀錄" 
        verbose_name_plural = "推播警告紀錄管理"
        ordering = ('created_at',)
