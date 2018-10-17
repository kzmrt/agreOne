from django.db import models
from django.urls import reverse
from datetime import datetime as dt
import uuid as uuid_lib


class Location(models.Model):
    """ロケーションモデル"""
    class Meta:
        db_table = 'location'

    name = models.CharField(verbose_name='ロケーション名', max_length=255)
    memo = models.CharField(verbose_name='メモ', max_length=255, default='', blank=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/
        return reverse('monitor:index')


class Greenhouse(models.Model):
    """温室モデル"""
    class Meta:
        db_table = 'greenhouse'
        unique_together = (('location', 'data_datetime'),)

    # uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False) # PKとして有効だが容量が大きく、データサイズが大きくなると性能が悪くなる。
    # id = models.BigAutoField(primary_key=True) # bigint

    location = models.ForeignKey(Location, verbose_name='ロケーション', on_delete=models.PROTECT)
    data_datetime = models.DateTimeField(verbose_name='データ日時', default=dt.strptime('2001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
    temp_out = models.FloatField(verbose_name='temp_out')
    temp_in = models.FloatField(verbose_name='temp_in')
    temp_set = models.FloatField(verbose_name='temp_set')
    temp_vent = models.FloatField(verbose_name='temp_vent')
    temp_heat = models.FloatField(verbose_name='temp_heat')
    temp_soil = models.FloatField(verbose_name='temp_soil')
    rh_out = models.FloatField(verbose_name='rh_out')
    rh_in = models.FloatField(verbose_name='rh_in')
    rain = models.FloatField(verbose_name='rain')
    irradiance = models.FloatField(verbose_name='irradiance')
    co2_conc = models.FloatField(verbose_name='co2_conc')
    co2_set = models.FloatField(verbose_name='co2_set')
    net_photos = models.FloatField(verbose_name='net_photos')
    transpiration = models.FloatField(verbose_name='transpiration')
    head_load = models.FloatField(verbose_name='head_load')
    head_load_pu = models.FloatField(verbose_name='head_load_pu')
    control_mode = models.FloatField(verbose_name='control_mode')
    night_cool_mode = models.FloatField(verbose_name='night_cool_mode')
    window_opening = models.FloatField(verbose_name='window_opening')
    window_kp = models.FloatField(verbose_name='window_kp')
    curtain_mode = models.FloatField(verbose_name='curtain_mode')
    hp_heat = models.FloatField(verbose_name='hp_heat')
    hp_cool = models.FloatField(verbose_name='hp_cool')
    hf = models.FloatField(verbose_name='hf')
    mist = models.FloatField(verbose_name='mist')
    exhaust_fun = models.FloatField(verbose_name='exhaust_fun')
    co2 = models.FloatField(verbose_name='co2')
    co2_sec = models.FloatField(verbose_name='co2_sec')
    dehumidify = models.FloatField(verbose_name='dehumidify')
    fan_mode = models.FloatField(verbose_name='fan_mode')
    fan_speed = models.FloatField(verbose_name='fan_speed')
    shutter = models.FloatField(verbose_name='shutter')
    fan2_mode = models.FloatField(verbose_name='fan2_mode')
    fan2_speed = models.FloatField(verbose_name='fan2_speed')
    shutter2 = models.FloatField(verbose_name='shutter2')
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.location.name + ":" + str(self.data_datetime)