from django.urls import path
from . import views

app_name = 'monitor'

urlpatterns = [
    # トップ画面
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # 詳細画面
    path('monitor/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /monitor/help/
    path('monitor/help/', views.help, name='help'),
]