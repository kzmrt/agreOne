from django import forms

class MyForm(forms.Form):
    start = forms.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"], label='開始日時')
    end = forms.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"], label='終了日時')

