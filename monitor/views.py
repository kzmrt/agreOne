from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Location
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

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


class IndexView(LoginRequiredMixin, generic.ListView): # generic.ListViewを継承
    model = Location # 使用するモデル
    paginate_by = 5  # 1ページあたりの表示件数をカスタマイズ
    ordering = ['-updated_at']  # 並び順を更新時刻が新しい順にカスタマイズ
    template_name = 'monitor/index.html'  # 表示に使用するテンプレート


class DetailView(generic.DetailView):
    model = Location
    template_name = 'monitor/detail.html'


@login_required
def help(request):
    return HttpResponse("Member Only Help Page")