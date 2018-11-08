from django import forms
from .models import Greenhouse
import bootstrap_datepicker_plus as datetimepicker
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime as dt, timedelta


class GreenhouseForm(forms.ModelForm):
    class Meta:
        model = Greenhouse
        fields = ('data_datetime',)
        widgets = {
            # スマホ対応版 キーボード入力不可
            'data_datetime': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ),
        }


class SampleForm(forms.Form):

    start_date = forms.DateField(
        label='開始日時',
        widget=datetimepicker.DateTimePickerInput(
            format='%Y/%m/%d %H:%M:%S',
            #attrs={'readonly': 'true'}, # テキストボックス直接入力不可
            #attrs={'class': 'form-control'},
            options={
                'locale': 'ja',
                'dayViewHeaderFormat': 'YYYY年 MMMM',
                'ignoreReadonly': True,
                'allowInputToggle': True,
                'minDate': '2018/10/22', # 最小日時（データ取得開始日）
            }
        ).start_of('term'),
    )
    end_date = forms.DateField(
        label='終了日時',
        initial=dt.now().strftime('%Y/%m/%d %H:%M:%S'),  # 初期値
        widget=datetimepicker.DateTimePickerInput(
            format='%Y/%m/%d %H:%M:%S',
            #attrs={'readonly': 'true'}, # テキストボックス直接入力不可
            options={
                'locale': 'ja',
                'dayViewHeaderFormat': 'YYYY年 MMMM',
                'ignoreReadonly': True,
                'allowInputToggle': True,
                'maxDate': (dt.now() + timedelta(days = 1)).strftime('%Y/%m/%d %H:%M:%S'),  # 最大日時（翌日）
            }
        ).end_of('term'),
    )