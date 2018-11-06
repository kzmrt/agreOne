from django import forms
from .models import Greenhouse
import bootstrap_datepicker_plus as datetimepicker
from bootstrap_datepicker_plus import DatePickerInput


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


class ToDoForm(forms.Form):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    date = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
    )