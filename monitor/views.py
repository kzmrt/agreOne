from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Location, Greenhouse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import random
import io
import matplotlib.pyplot as plt
import numpy as np
import logging
from monitor import db


"""
Django Auth
The LoginRequired mixin
https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-loginrequired-mixin
The login_required decorator
https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
@login_required
"""

'''
def index(request):
    return HttpResponse("Hello, world. You're at the monitor index.")
'''
logger = logging.getLogger('development')


class IndexView(LoginRequiredMixin, generic.ListView): # generic.ListViewを継承
    model = Location # 使用するモデル
    paginate_by = 5  # 1ページあたりの表示件数をカスタマイズ
    ordering = ['-updated_at']  # 並び順を更新時刻が新しい順にカスタマイズ
    template_name = 'monitor/index.html'  # 表示に使用するテンプレート


class DetailView(generic.DetailView):
    model = Location
    template_name = 'monitor/detail.html'

"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す

        # データの絞り込み（pkおよび日時の範囲）
        start_date = datetime.datetime(2018, 10, 22, 10, 15, 00)
        end_date = datetime.datetime(2018, 10, 22, 18, 45, 00)
        green = Greenhouse.objects.select_related('location').filter(location_id=self.kwargs['pk'],
                                                                     data_datetime__range=(start_date, end_date))
        # green = Greenhouse.objects.filter(location_id=self.kwargs['pk'], data_datetime__range=(start_date, end_date))
        #green = Greenhouse.objects.filter(location_id=self.kwargs['pk'])
        #logger.info("データサイズ：" + str(len(green)))
        context['greenhouse_data_list'] = green

        return context
"""

@login_required
def help(request):
    return HttpResponse("Member Only Help Page")


# グラフ作成
def setPlt(pk):
    start = '2018-10-22 10:15:00'
    end = '2018-10-22 18:45:00'
    x = []
    y = []
    for data in db.getDbRecord.getGreenhouseRecord(pk, start_datetime=start, end_datetime=end): # DBレコード取得
        print(data[2])
        x.append(data[2])
        y.append(data[3])

    plt.plot(x, y)

    # グラフの体裁
    fsz = 6
    plt.rcParams["font.size"] = fsz
    plt.rcParams['font.family'] = 'sans-serif'
    fti = 15  # タイトルのフォントサイズ
    plt.title('Title', loc='left', fontsize=fti)


# svgへの変換
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s


@login_required
def get_svg(request,  pk):
    setPlt(pk) # create the plot
    svg = pltToSvg() # convert plot to SVG
    plt.cla() # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

