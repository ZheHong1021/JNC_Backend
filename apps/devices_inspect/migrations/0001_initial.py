# Generated by Django 4.2.5 on 2023-10-03 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessTokenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Token使用的場')),
                ('token', models.TextField(verbose_name='Token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='創立時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改時間')),
            ],
            options={
                'verbose_name': '推播權杖儲存',
                'verbose_name_plural': '推播權杖儲存管理',
                'db_table': 'access_token',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='JNCDeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeviceName', models.CharField(max_length=255, verbose_name='設備名稱')),
                ('JNCDevice', models.CharField(max_length=255, verbose_name='設備項目(I6_Web、Feeder、Weather_Station、CloudBox、VirtualDevice)')),
                ('GPSx', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='經度(Longitude)')),
                ('GPSy', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='緯度(Latitude)')),
                ('Connect', models.BooleanField(verbose_name='有無連線')),
                ('USB', models.IntegerField(verbose_name='(-1、0、2、3)')),
                ('SIM', models.IntegerField(verbose_name='(-1、0、4、10)')),
                ('device_url', models.TextField(verbose_name='設備API url')),
                ('inspect_url', models.TextField(verbose_name='檢測API url')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='創立時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改時間')),
                ('token_id', models.ForeignKey(db_column='token_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='devices_inspect.accesstokenmodel')),
            ],
            options={
                'verbose_name': '檢測設備列表',
                'verbose_name_plural': '檢測設備管理',
                'db_table': 'jnc_devices',
                'ordering': ('created_at',),
            },
        ),
    ]
