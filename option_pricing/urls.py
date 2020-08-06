from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name="home"),
    path('paginate_test_1/', views.paginate_test_1, name='paginate_test_1'),
    path('bootstrap_filter/', views.BootstrapFilterView, name='bootstrap_filter'),
    path('<int:pk>/', views.OptionDetailView, name='option_detail'),
    path('optionftse/', views.OptionFtseView, name='option_ftse'),
    path('optionftse/<slug:optionsymbol>/', views.OptionFtseViewDetail, name='option_ftse_strikespan'),
    path('zingchart/<str:stock>/', views.zingchartView, name="zingchart"),
    path('zingchart/bar/<slug:tradesymbol>/', views.zingchartView1, name="zingchart1"),
    path('zingchart/chart/<str:obj>/', views.zingchartView2, name="zingchart2"),
    path('jschart/<str:optionsymbol>/', views.JSChartView, name='js_chart'),
    path('jschart/chart/<str:tradesymbol>/', views.JSChartView1, name="js_chart1"),
]