from django.urls import path
from . import views

app_name = 'monitor'

urlpatterns = [
    # トップ画面
    path('', views.IndexView.as_view(), name='index'),

    # 詳細画面
    path('monitor/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # グラフ描画
    path("monitor/<int:pk>/chart/", views.update_chart, name='chart'),
    path("monitor/<int:pk>/plot/", views.update_plot, name='plot'),

    # パスワード変更画面
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),

    # ex: /monitor/help/
    path('monitor/help/', views.help, name='help'),
]