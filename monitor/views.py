from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Location, Greenhouse
from django.contrib.auth.decorators import login_required
#from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import logging
#from monitor import db
#from .forms import MyForm


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

x = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
y = [12, 19, 30, 50, 20, 30]

class IndexView(LoginRequiredMixin, generic.ListView): # generic.ListViewを継承
    model = Location
    paginate_by = 5
    ordering = ['-updated_at']
    template_name = 'monitor/index.html'


class DetailView(generic.DetailView):
    model = Location
    template_name = 'monitor/detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # データの絞り込み（pkおよび日時の範囲）
        start_date = datetime.datetime(2018, 10, 22, 10, 15, 00)
        end_date = datetime.datetime(2018, 10, 22, 18, 45, 00)
        #green = Greenhouse.objects.select_related('location').filter(location_id=self.kwargs['pk'],
        #                                                            data_datetime__range=(start_date, end_date))
        #green = db.getDbRecord.getGreenhouseRecord(self.kwargs['pk'], start_datetime=start_date, end_datetime=end_date)

        """
                green = [12, 19, 30, 50, 20, 30]
                context['greenhouse_data_list'] = green

                start = '2018-10-22 15:15:00'
                end = '2018-10-22 18:45:00'
                x = []
                y = []
                for data in db.getDbRecord.getGreenhouseRecord(self.kwargs['pk'], start_datetime=start, end_datetime=end):  # DBレコード取得
                    x.append(data[2].strftime('%Y/%m/%d %H:%M:%S'))
                    #x.append(data[0])
                    y.append(data[3])
        """

        context['x_data'] = x
        context['y_data'] = y

        return context


def update_chart(request, pk):

    input_text_data = request.POST.getlist("input_data") # 入力した値を取得

    y[0] = int(input_text_data[0]) # 一つ目のデータを入力値に更新する
    #y[1] = pk
    y_data = y
    x_data = x
    return render(request, 'monitor/chart.html', {'y_data': y_data, 'x_data': x_data})


@login_required
def help(request):
    return HttpResponse("Member Only Help Page")






